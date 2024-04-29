## Flask Application Design for Kids' Planner

### HTML Files

**1. index.html (Homepage)**
- Presents an overview of the planner and its features.
- Lists the child profiles and their respective schedules.
- Provides a form to create new profiles and events.

**2. profile.html (Child Profile)**
- Displays a specific child's schedule in detail.
- Allows editing of the child's name and age.
- Includes options to add, remove, and modify events.

**3. event_form.html (Event Creation and Editing)**
- Provides a form to create or edit events.
- Collects details like event name, date, time, and category (e.g., Music, Sports, Homework).

### Routes

**1. / (Homepage)**
- Serves the `index.html` file.

**2. /profile/<child_id> (Child Profile)**
- Serves the `profile.html` file and provides data for the specific child based on the `child_id`.

**3. /create_profile (Create Child Profile)**
- Handles the creation of new child profiles using data from the `index.html` form.
- Redirects to `/` upon successful creation.

**4. /edit_profile/<child_id> (Edit Child Profile)**
- Handles editing of existing child profiles using data from the `profile.html` form.
- Redirects to `/profile/<child_id>` upon successful update.

**5. /create_event/<child_id> (Create Event)**
- Handles the creation of new events for a specific child using data from the `event_form.html` form.
- Redirects to `/profile/<child_id>` upon successful creation.

**6. /edit_event/<event_id> (Edit Event)**
- Handles editing of existing events using data from the `event_form.html` form.
- Redirects to `/profile/<child_id>` upon successful update, where `child_id` is the parent of the event.

**7. /delete_event/<event_id> (Delete Event)**
- Handles the deletion of existing events.
- Redirects to `/profile/<child_id>` upon successful deletion, where `child_id` is the parent of the event.