import React, { useState } from 'react';
import { Form, Button } from 'semantic-ui-react';
import axios from 'axios';

export const Settings = ({ user, onClose }) => {
  const [formData, setFormData] = useState({
    notifications: user.notifications || false,
    privacy: user.privacy || 'public',
  });

  const handleChange = (e, { name, value }) => {
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleCheckboxChange = (e, { name, checked }) => {
    setFormData((prevData) => ({
      ...prevData,
      [name]: checked,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const updatedSettings = {
        ...user,
        notifications: formData.notifications,
        privacy: formData.privacy,
      };
      await axios.put(`/users/${user.id}/settings`, updatedSettings);
      onClose();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Checkbox
        label="Enable Notifications"
        name="notifications"
        checked={formData.notifications}
        onChange={handleCheckboxChange}
      />
      <Form.Select
        label="Privacy Settings"
        name="privacy"
        options={[
          { key: 'public', text: 'Public', value: 'public' },
          { key: 'private', text: 'Private', value: 'private' },
        ]}
        value={formData.privacy}
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
