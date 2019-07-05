# Hannah Chebet Photo
*Photography portfolio with Django*

## Overview

This photography portfolio and blog was created using Photova, a Django based photography portfolio template. https://github.com/tateshep/Photova

## Features

- Gallery
- Blog
- Email
- Comments
- Admin

### Gallery

- File upload and display
- Images stored to db via file upload
- Organize Images by Collection
- Update/edit views for admin users 
- Show case galleries for portfolio display
- Private galleries for clients, with download functionality

##### Usage

Admin users can upload images. They must have "is_staff" set on their user account. These images get stored to the database, but are not immediately displayed on the website until they have been included in a Collection. Collections are groupings of images according to the photographers preference or categorization. Admin users can create collections from the django admin, website admin interface, or from the "Gallery" page. These collections may then be selected for the "Showcase Gallery" which will make them publicly visible. The images that are to be included in the collection are selected in the "create collection" form. Additionally, any Permitted Users may be selected. The permitted users will be able to view the collection from their "My Collections" page. This allows private collections to be shared with potential clients from the photographer using the following steps; A photographer creates a collection, but leaves the Showcase Gallery option unchecked. The photographer then chooses which user(s) will be allowed to view the collection when they are logged in. Users with collections in "My Collections" will be allowed to download images here. All other users will be unable to view the private collection. Collections with the Showcase Gallery option checked are automatically added to the Gallery page, and should be considered the photographer's public portfolio.

Collections and Images can both be edited, or deleted from their detail views and from the admin view. The buttons for these views as well as the views themselves are accessible to admin users only.

### Blog

##### Capabilities
- New Blog Post
- View Blog Post
- Update Blog Post
- Delete Blog Post
- Staff permission required

##### Usage
 
The first page a user reaches when using the blog feature is a blog index view. This is a list of all blog posts organized by creation date. Blog posts are comprised of a thumbnail image, title, text body content, and a group of images pertaining to the post. Creating a blog post is simple. An admin user will be presented with an "Add Post" button at the bottom of the blog index view. Normal users can not add, edit, or delete posts. A form allows the user to input the title, thumbnail image, text body, and images. The thumbnail image is displayed on the blog card in the index view. From the index view, a user may select a post to read the entire content and view the other post images. To edit or delete posts, an admin user can select a post, visiting its detail view, and then choose the relevant button at the bottom page to perfom the desired changes.

### Email

##### Accessible from:
- Contact Form

##### Usage

The email functionality is still in development, awaiting the configuration of a SMTP service provider. Presently, if a user utilizes the contact form, a response may be viewed in the server log detailing the Subject, From Email, To Email, and message content.



### Comments

##### Available For:
- Blog Posts
- Collections
- Images
- Login required

##### Usage

The comment feature has been included for the following; Blog Posts, Collections, and Images. This allows clients to provide publicly viewable feedback to the photographer. Users must have an account to write comments, but the comments are viewable to any visitor of the site provided they are not in a private collection.

### Admin

##### Available for:
- Collections
- Images
- Blog Posts
- Users (view only)
- Staff permissions required

##### Usage

The admin view is a shortcut view to access all the admin capabilities from one place. From this page, admin users can view, update, or delete any of the following; Collections, Images, and Blog Posts. A list of all the user accounts is also accessible from this view, allthough any edits to users must be made through the django admin.
