import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { Grid, Card, Image } from 'semantic-ui-react';

export const UserGrid = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  const getUsers = async () => {
    const response = await axios.get('/users');
    console.log('RESPONSE DATA: ', response.data);
    setUsers(response.data);
  };

  useEffect(() => {
    setLoading(true);
    getUsers();
    setLoading(false);
  }, []);

  return (
    <Grid columns={3} stackable>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <Grid.Row>
          {users.map((user) => (
            <Grid.Column key={user.id}>
              <Card as={Link} to={`/profile/${user.id}`}>
                <Image
                  src={user.imageUrl}
                  alt={'Photo of ' + user.name}
                  wrapped
                  ui={false}
                />
                <Card.Content>
                  <Card.Header>{user.name}</Card.Header>
                  <Card.Description>{user.about}</Card.Description>
                </Card.Content>
              </Card>
            </Grid.Column>
          ))}
        </Grid.Row>
      )}
    </Grid>
  );
};
