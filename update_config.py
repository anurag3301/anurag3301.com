import os

def update_config():
    # Define the local and production base URLs
    local_base_url = "http://127.0.0.1:5000/blog"
    production_base_url = "http://anurag3301.com/blog"
    
    # Determine the base URL based on the environment
    base_url = local_base_url if os.getenv('FLASK_ENV') == 'development' else production_base_url
    
    # Read the config file
    with open('blog/config.toml.base', 'r') as file:
        config_content = file.read()
    
    # Replace the placeholder with the actual base URL
    config_content = config_content.replace("{BASE_URL}", base_url)
    
    # Write the updated content back to the config file
    with open('blog/config.toml', 'w') as file:
        file.write(config_content)

if __name__ == "__main__":
    update_config()
