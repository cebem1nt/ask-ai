#!/bin/bash

# creating venv and installing packages
echo 'Creating virtual environment...'
python3 -m venv venv

current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
venv_dir="$current_dir/venv/bin"

echo 'Sourcing to virtual environment...'
source "$venv_dir/activate"

echo 'Installing packages...'
pip3 install -r requirements.txt

echo 'Leaving virtual environment...'
deactivate

# requiring and storing API key
store_key() {
    local key="$1"
    local dir="${2:-askai}"
    local file="${3:-key.ini}"
    local full_dir="$HOME/.config/$dir"
    mkdir -p "$full_dir"
    
    cat <<EOF > "$full_dir/$file"
[KEY]
key = $key
EOF
}

read -p "Enter your api key: " API_KEY
store_key "$API_KEY"

echo "Adding shortcut to /usr/bin..."

#usr/bin/askai script for running
script="#!/bin/bash\nsource $venv_dir/activate\npython3 $current_dir/askai.py \"\$@\"\ndeactivate"

# Write the script to /usr/bin/askai
echo -e "$script" | sudo tee /usr/bin/askai > /dev/null
sudo chmod +x /usr/bin/askai

echo "Finished!"