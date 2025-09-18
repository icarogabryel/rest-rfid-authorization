# 🪪 RFID Authorization REST API

This is a simple RESTful API for managing RFID card authorization to study single app minimalist Django project structure.

## 🧩 Business Rules

Each RFID card registered in the system has an access level. The embedded systems will be the edge nodes and each will have inside their firmware the minimum access level required to enter a specific area. The edge nodes can retrieve a specific card to check its access level, create a new card, update the access level of an existing card or delete a card.

## 🚪 Access Levels

The access levels are like the Resident Evil 2 video game, where the player can find different access electronic chips to open doors with different colors. The access levels are:

- <span style="color:green">GREEN</span>: can open <span style="color:green">GREEN</span> doors
- <span style="color:blue">BLUE</span>: can open <span style="color:green">GREEN</span> and <span style="color:blue">BLUE</span> doors
- <span style="color:purple">PURPLE</span>: can open <span style="color:green">GREEN</span>, <span style="color:blue">BLUE</span> and <span style="color:purple">PURPLE</span> doors

## 🌐 API Endpoints

- Create Card
  - Path: `/card/`
  - Method: `POST`
  - Request body:

    ```json
    {
    "id": "string",
    "access_level": "string",
    }
    ```

  - Response code: 201 Created
  - Response body:

    ```json
    {
    "id": "string",
    "access_level": "string",
    }
    ```

- Retrieve Card
  - Path: `/card/{id}/`
  - Method: `GET`

  - Response code: 200 OK
  - Response body:

    ```json
    {
    "id": "string",
    "access_level": "string",
    }
    ```

- Update Card
  - Path: `/card/{id}/`
  - Method: `PUT`
  - Request body:

    ```json
    {
      "access_level": "string",
    }
    ```

  - Response code: 200 OK
  - Response body:

    ```json
    {
    "id": "string",
    "access_level": "string",
    }
    ```

- Destroy Card
  - Path: `/card/{id}/`
  - Method: `DELETE`
  - Response code: 204 No Content
