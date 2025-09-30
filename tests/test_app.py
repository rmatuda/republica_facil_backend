from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@example.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/999',  # ID inexistente
        json={
            'username': 'naoexiste',
            'email': 'naoexiste@example.com',
            'password': 'qualquer',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user_not_found(client):
    response = client.delete('/users/999')  # ID inexistente
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_user(client):
    # Cria usuário
    client.post(
        '/users/',
        json={
            'username': 'uniqueuser',
            'email': 'unique@example.com',
            'password': 'senha',
        },
    )
    # Busca usuário existente
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'uniqueuser',
        'email': 'unique@example.com',
        'id': 1,
    }


def test_read_user_not_found(client):
    response = client.get('/users/999')  # ID inexistente
    assert response.status_code == HTTPStatus.NOT_FOUND
