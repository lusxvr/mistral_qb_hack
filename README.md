# Mistral QB Hackathon

This project was built during the 2-day Mistral-Quantum Black Hackathon at école polytechnique in Paris, by Diane Mansard, Felix Müller, [Luis Wiedmann](https://www.linkedin.com/in/luis-wiedmann/) and [Jan Dorn](https://www.linkedin.com/in/jandorn/).

## Overview

The goal of the hackathon was to build a retail assistant using LLMs provided by Mistral. It was not specified what kind of product to sell, so early on we decided to build a travel planner that helps users find the perfect trip and then sells it to them.

Through a user-friendly webapp, the user can input their preferences using some default filters and a free-text field. The webapp then uses the LLM to find the perfect trip and displays it to the user.

## Installation
To lauch the app locally, we have to spin up a local webserver for the webapp and the backend.

### Webapp
From the `webapp` directory, run 

```
npm install
npm run dev
```

This will launch the webapp on `localhost:5173`.

### Backend
From the `backend` directory, run (if desired in a virtual environment)

```
pip install -r requirements.txt
fastapi dev
```

The backend needs some API keys to be set in the environment variables to work. Create a `.env` file in the root directory and prepare your keys for the following services:

- TAVILY_API_KEY="..."
    - see https://www.tavily.com/
- MISTRAL_API_KEY="..."
    - see https://mistral.ai/
- AMADEUS_CLIENT_ID="..."
    - see https://developers.amadeus.com/
- AMADEUS_CLIENT_SECRET="..."
    - see https://developers.amadeus.com/
- OPENWEATHERMAP_API_KEY="..."
    - see https://openweathermap.org/

## Project Architecture

The following diagram shows the architecture of the project.

![Project Architecture](./misc/architecture.png)

## Webapp

## Backend