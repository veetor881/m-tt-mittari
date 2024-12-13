# Create the virtual environment
echo "Creating virtual environment..."
virtualenv mättö_env

# Activate the virtual environment
echo "Activating virtual environment..."
source mättö_env/bin/activate

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete! Virtual environment is ready."
