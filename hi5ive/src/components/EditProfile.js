import React, { useState } from 'react';
import { Form, Button } from 'semantic-ui-react';
import axios from 'axios';

export const EditProfile = ({ user, onClose }) => {
  const [formData, setFormData] = useState({
    name: user.name,
    imageUrl: user.imageUrl,
    about: user.about,
    hobbies: user.hobbies.join(', '),
    groups: user.groups.join(', '),
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const updatedUser = {
        ...user,
        name: formData.name,
        imageUrl: formData.imageUrl,
        about: formData.about,
        hobbies: formData.hobbies.split(', '),
        groups: formData.groups.split(', '),
      };
      await axios.put(`/users/${user.id}`, updatedUser);
      onClose();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Input
        label="Name"
        name="name"
        value={formData.name}
        onChange={handleChange}
      />
      <Form.Input
        label="Profile Picture URL"
        name="imageUrl"
        value={formData.imageUrl}
        onChange={handleChange}
      />
      <Form.TextArea
        label="About Me"
        name="about"
        value={formData.about}
        onChange={handleChange}
      />
      <Form.Input
        label="Hobbies (comma separated)"
        name="hobbies"
        value={formData.hobbies}
        onChange={handleChange}
      />
      <Form.Input
        label="Groups (comma separated)"
        name="groups"
        value={formData.groups}
        onChange={handleChange}
      />
      <Button type="submit" primary>
        Save
      </Button>
      <Button type="button" onClick={onClose}>
        Cancel
      </Button>
    </Form>
  );
};
