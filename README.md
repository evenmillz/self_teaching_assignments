# Self-Teaching Assignments

This repository documents the hands-on journey through a self-paced learning sprint focused on essential backend and API development concepts using Python and supporting tools. Each folder in this repository represents a targeted assignment or challenge designed to build real-world technical fluency.

## Repository Structure

### `connexion_api_challenge/`

- Built a working RESTful API using the Connexion framework with OpenAPI 3.0 specification.
- Integrated Swagger UI for interactive documentation.
- Connected to JSONPlaceholder mock API to simulate fetching post data by ID.

### `requests_challenge/`

- Wrote a Python script that utilizes the `requests` library to fetch and print posts from the JSONPlaceholder API.
- Demonstrated asynchronous and programmatic API interaction using basic HTTP GET requests.

### `yaml_challenge/`

- Explored the YAML data format and created custom configuration files.
- Used both `PyYAML` and `ruamel.yaml` Python packages to load and parse YAML.
- Learned about the importance of structured configuration management in software projects.

### `cURL_challenge/`

- Practiced command-line HTTP requests using `curl`.
- Retrieved and saved raw HTML pages using `curl` commands.
- Developed foundational understanding of how web servers and endpoints communicate.

### `flask_challenge/`

- Installed Flask and served a basic HTML page from a Python script.
- Learned about routing, request handling, and local development servers.

## Skills Gained

- RESTful API development with Connexion & Flask
- YAML syntax and Python integration
- Python HTTP requests with `requests`
- Command-line HTTP interactions using `curl`
- API interaction using Postman
- Swagger / OpenAPI documentation
- JSONPlaceholder mock API exploration

## Purpose

This repo serves as a launchpad for transitioning into real-world backend API work, understanding service communication, and integrating documentation tools. All assignments are geared toward building confidence with tools that power modern web development and data exchange.

---

Designed and implemented with intention by Even Richardson.

---

## How to Use This Repository

Each folder in this repository is a standalone exercise and can be run independently. To get started with any assignment:

1. **Clone the repository**

   ```bash
   git clone https://github.com/evenmillz/self_teaching_assignments.git
   cd self_teaching_assignments
   ```

2. **Navigate to a challenge directory**  
   For example, to explore the YAML assignment:

   ```bash
   cd yaml_challenge
   ```

3. **Run the scripts**  
   Most challenges are self-contained Python scripts. For example:

   ```bash
   python read_yaml.py
   ```

4. **View Swagger UI (if using Connexion)**  
   For the `connexion_api_challenge`, run the app:

   ```bash
   cd connexion_api_challenge
   python app.py
   ```

   Then open your browser to [http://localhost:5000/ui](http://localhost:5000/ui) to explore the API docs.

5. **Try the cURL commands**  
   In the `cURL_challenge` folder, use the terminal to run:

   ```bash
   curl https://example.com > output.html
   ```

6. **Postman Challenge**  
   The Postman portion uses the [JSONPlaceholder API](https://jsonplaceholder.typicode.com). Import endpoints into Postman and test GET, POST, PUT, and DELETE methods.

> No external setup is required beyond Python 3 and `pip install -r requirements.txt` (if included).

---

Feel free to explore each folder and experiment. This repo is meant to be broken, rebuilt, and learned from.
