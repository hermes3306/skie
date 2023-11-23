#find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/7687/7689/g' {} +
find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/7689/7687/g' {} +

find . -type f -name "*.sh" ! -name "0.portchange.sh" -exec sed -i 's/localhost/vm/g' {} +
