# task4.sh - print system information

echo "Kernel Version:"
uname -r
echo

echo "User:"
whoami
echo

echo "Hardware Virtualization Info:"
if command -v lscpu >/dev/null 2>&1; then
    lscpu | grep -i 'Virtualization' || echo "No virtualization entry found."
else
    echo "lscpu not found."
fi
