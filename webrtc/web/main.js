const startButton = document.getElementById('startButton');
const hangupButton = document.getElementById('hangupButton');
let localStream, pc1, pc2;

startButton.addEventListener('click', startCall);
hangupButton.addEventListener('click', hangUp);

async function startCall() {
    localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

    document.getElementById('localVideo').srcObject = localStream;

    const configuration = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] };

    pc1 = new RTCPeerConnection(configuration);
    pc2 = new RTCPeerConnection(configuration);

    // Add local stream to pc1
    localStream.getTracks().forEach(track => pc1.addTrack(track, localStream));

    // Set up event handlers
    pc1.onicecandidate = e => onIceCandidate(pc1, pc2, e);
    pc2.onicecandidate = e => onIceCandidate(pc2, pc1, e);
    pc2.ontrack = e => onTrack(e);

    // Create offer and set local description for pc1
    const offer = await pc1.createOffer();
    await pc1.setLocalDescription(offer);
    await pc2.setRemoteDescription(offer);

    // Create answer and set local description for pc2
    const answer = await pc2.createAnswer();
    await pc2.setLocalDescription(answer);
    await pc1.setRemoteDescription(answer);
}

function onIceCandidate(pc, otherPc, event) {
    if (event.candidate) {
        otherPc.addIceCandidate(new RTCIceCandidate(event.candidate));
    }
}

function onTrack(event) {
    document.getElementById('remoteVideo').srcObject = event.streams[0];
}

function hangUp() {
    pc1.close();
    pc2.close();
    localStream.getTracks().forEach(track => track.stop());
    document.getElementById('remoteVideo').srcObject = null;
}

