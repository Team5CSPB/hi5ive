import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
//import axios from 'axios';
import { Grid, Card, Image,Button,Icon} from 'semantic-ui-react';
import DummyData from '../DummyData.json'; // Import your JSON data


// sample user interests data


export const UserGrid = ({ searchTerm ,onMatch}) => {
  console.log('Search Term:', searchTerm);
  const [users, setUsers] = useState(DummyData);
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log('Dummy Data:', DummyData); // Debugging
    setLoading(true);
    setUsers(DummyData);
    setFilteredUsers(DummyData);
    setLoading(false);
  }, []);

  useEffect(() => {
    filterUsers();
  }, [searchTerm]);

  const filterUsers = () => {
    const term = searchTerm.toLowerCase();
    const filtered = users.filter(user => {
      // Check if the search term matches any of the user's interests
      const hasMatchingInterest = user.interests.some(interest =>
        interest.toLowerCase().includes(term)
      );
      return hasMatchingInterest;
    });

    setFilteredUsers(filtered);
  };

  return (
    <Grid columns={3} stackable>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <Grid.Row>
          {filteredUsers.length > 0 ? (
            filteredUsers.map(user => (
              <Grid.Column key={user.username}>
                <Card as={Link} to={`/profile/${user.username}`}>
                  <Image
                    src={user.profile_pic} // Ensure this path is correct
                    alt={'Photo of ' + user.firstname + ' ' + user.lastname}
                    wrapped
                    ui={false}
                  />
                  <Card.Content>
                    <Card.Header>{user.firstname} {user.lastname}</Card.Header>
                    <Card.Description>{user.bio}</Card.Description>
                  </Card.Content>
                  <Card.Content extra>
                    <Button icon labelPosition='right'>
                      Match
                      <Icon name='handshake' />
                    </Button>
                  </Card.Content>
                </Card>
              </Grid.Column>
            ))
          ) : (
            <p>No users found.</p>
          )}
        </Grid.Row>
      )}
    </Grid>
  );
};