# Daily Quotes Service

This project provides a serverless backend for a daily quotes service, along with a simple frontend using Next.js.

## Setup Instructions

### Backend Setup

1. **Install Serverless Framework**:
    ```sh
    npm install -g serverless
    ```

2. **Create a new Serverless project**:
    ```sh
    serverless
    ```
    - Select `python starter api` or `python flask with dynamo`.
    - Choose `Python 3.12`.
    - Open the project in VS Code:
        ```sh
        code .
        ```

3. **Create Handlers**:
    - Create a `handler` folder in the project.
    - Create the following Python files in the `handler` folder:

        - `getQuotes.py`: Fetches quotes from S3 and renders via API Gateway.
        - `subscribeUser.py`: Adds subscribers to DynamoDB.
        - `getSubscribers.py`: Fetches subscriber details from DynamoDB.
        - `staticMailer.py`: Sends email notifications using AWS SNS.
        - `sendEmail.py`: Sends emails via SendGrid platform.

4. **Modify `serverless.yml`**:
    - Define the functions for each of the above handlers.
    - Add layers for SendGrid and requests libraries.

5. **Deploy the Project**:
    ```sh
    serverless deploy --verbose
    ```

### Frontend Setup

1. **Set up the project**:
    ```sh
    mkdir quotes-site
    cd quotes-site
    npm install axios
    npm install next@14.2.5 react@18.2.0 react-dom@18.2.0 --force
    npx create-next-app quotes-site --use-npm --example "https://github.com/vercel/next-learn/tree/1011f2f19fc821f09d2ec685e42229d0826fca71/basics/learn-starter"
    ```

2. **Run the development server**:
    ```sh
    npm run dev
    ```
    - The frontend should be available at [http://localhost:3000](http://localhost:3000).

## API Endpoints

- **GET** `/quotes` - Fetches the quotes from S3.
- **POST** `/subscribe` - Adds a subscriber to the DynamoDB table.
- **GET** `/subscribers` - Fetches the subscriber details.
- **POST** `/mailer` - Sends email notifications via AWS SNS.
- **POST** `/sendEmail` - Sends daily quotes via SendGrid (scheduled).

## Email Notifications

1. **Create a SendGrid account** and generate an API key.
2. **Add the API key to `serverless.yml`** as an environment variable.
3. **Add layers for SendGrid and requests libraries** to Lambda functions.
4. **Deploy the project** to test email notifications and scheduling.

---

**Note**: Replace placeholders like `your-bucket-name`, `your-email@example.com`, `your-sendgrid-api-key`, and `YourTopic` with actual values.

