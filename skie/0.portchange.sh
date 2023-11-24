#find -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/7687/7689/g' {} +
find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/7689/7687/g' {} +

#find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/localhost/vm/g' {} +
find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/neo4j:/neo4j+s:/g' {} +
find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/vm/942801e8.databases.neo4j.io/g' {} +
find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/re91na00/rPNgDfFeruVONoEH1Vc8JgsnukQLVKadEQJ5dtlCsaI/g' {} +
