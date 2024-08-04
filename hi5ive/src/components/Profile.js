import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import {
  Image,
  Segment,
  Grid,
  Header,
  Button,
  Icon,
  Modal,
  Card,
  Container,
} from 'semantic-ui-react';
import { EditProfile } from './EditProfile';
import { Settings } from './Settings';

import '../styles/style.css';

export const Profile = ({ user: loggedInUser }) => {
  const { userId } = useParams();
  const [user, setUser] = useState(loggedInUser || null);
  const [isEditProfileOpen, setIsEditProfileOpen] = useState(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);

  useEffect(() => {
    if (!loggedInUser) {
      const fetchUser = async () => {
        try {
          const response = await axios.get(`/users/${userId}`);
          setUser(response.data);
        } catch (error) {
          console.error(error);
        }
      };
      fetchUser();
    }
  }, [userId, loggedInUser]);

  return (
    user && (
      <Container className="profile-container">
        <Segment>
          <Grid>
            <Grid.Row>
              <Grid.Column width={6} textAlign="center">
                <Image
                  src={user.imageUrl}
                  alt={`Photo of ${user.name}`}
                  size="medium"
                  circular
                />
                <Header as="h2">
                  {user.name}
                  <Icon
                    color={user.status === 'active' ? 'green' : 'red'}
                    name="circle"
                  />
                </Header>
                <Button primary onClick={() => setIsEditProfileOpen(true)}>
                  Edit Profile
                </Button>
                <Button secondary onClick={() => setIsSettingsOpen(true)}>
                  Settings
                </Button>
              </Grid.Column>
              <Grid.Column width={10}>
                <Segment>
                  <Header as="h3">About Me</Header>
                  <p>{user.about}</p>
                </Segment>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row>
              <Grid.Column width={16}>
                <Segment>
                  <Header as="h3" icon="heart" content="Hobbies" />
                  <Card.Group itemsPerRow={3}>
                    {user.hobbies.map((hobby, idx) => (
                      <Card key={idx}>
                        <Card.Content>
                          <Icon name="star" />
                          <Card.Header>{hobby}</Card.Header>
                        </Card.Content>
                      </Card>
                    ))}
                  </Card.Group>
                </Segment>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row>
              <Grid.Column width={16}>
                <Segment>
                  <Header as="h3" icon="users" content="Groups" />
                  <Card.Group itemsPerRow={3}>
                    {user.groups.map((group, idx) => (
                      <Card key={idx}>
                        <Card.Content>
                          <Icon name="group" />
                          <Card.Header>{group}</Card.Header>
                        </Card.Content>
                      </Card>
                    ))}
                  </Card.Group>
                </Segment>
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Segment>
        <Modal
          open={isEditProfileOpen}
          onClose={() => setIsEditProfileOpen(false)}
        >
          <Modal.Header>Edit Profile</Modal.Header>
          <Modal.Content>
            <EditProfile
              user={user}
              onClose={() => setIsEditProfileOpen(false)}
            />
          </Modal.Content>
        </Modal>
        <Modal open={isSettingsOpen} onClose={() => setIsSettingsOpen(false)}>
          <Modal.Header>Settings</Modal.Header>
          <Modal.Content>
            <Settings user={user} onClose={() => setIsSettingsOpen(false)} />
          </Modal.Content>
        </Modal>
      </Container>
    )
  );
};
