# Handbok for Burnout: Your Guide on the Recovery Journey

## Introduction
Handbok for Burnout is a supportive community app designed specifically for individuals experiencing burnout. This blog-style platform offers a curated collection of resources, including podcast recommendations, low-impact activities, meditations, and personalized routines to aid in recovery.

We understand that when one is experiencing burnout, even simple tasks like googling for tips can feel overwhelming. That’s why we’ve created Handbok for Burnout – to provide a curated list of suggestions all in one place, making the recovery journey easier and less stressful. You can think of it as a library only for burnout.

To foster a sense of community and ensure a safe, interactive space, users must register and log in to read and comment on activities. This collaborative feature encourages meaningful engagement and connection among members who understand the journey of overcoming burnout.

## Table of Contents
- [Introduction](#introduction)
- [UX](#ux)
- [Design](#design)
- [Features](#features)
    * [Future Features](#future-features)
- [Project Planning](#project-planning)
    * [Wireframes](#wireframes)
    *  [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
        - [Models](Models)
    - [Agile Methodologies ](#agile-methodologies)
        * [Epics](#epics)
        * [User stories](#user-stories)
        * [MoSCoW prioritization](#moscow-prioritization)
        * [Kanban board](#kanban-board)
    - [Technologies Used](#technologies-used)
        * [Languages](#languages)
        * [Frameworks](#frameworks)
        * [Libraries](#libraries)
        * [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
    * [GitHub](#github)
    * [Heroku](#heroku)
- [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)
    

## User Experience (UX)

The site is designed with a mobile-first approach, ensuring an optimal browsing experience on smartphones and tablets. This approach prioritizes fast load times, intuitive navigation, and responsive design, making the site accessible and user-friendly across all devices.

## Project planning

### Wireframes

Balsamiq was used to create detailed visual representations of the app's design. These wireframes helped in planning the layout and user interface, ensuring a user-friendly experience.

#### Mobile

![Index](documentation/readme_photos/mobile_index.png) 

![Index Menu](documentation/readme_photos/mobile_index_menu.png)

![Activity](documentation/readme_photos/mobile_activitiy.png)

![Activity Menu](documentation/readme_photos/mobile_activity_menu.png)

#### Tablet

![Index](documentation/readme_photos/tablet.png)

![Activity](documentation/readme_photos/tablet_activity.png)

### Database Schema - Entity Relationship Diagram

The database schema for the application is illustrated using an Entity Relationship Diagram (ERD). [Lucidchart](https://www.lucidchart.com/) was used to design the ERD, providing a clear visual representation of the database structure. This diagram outlines the relationships between different entities in the system, ensuring efficient data organization and retrieval. The ERD served as a crucial tool in planning the database, allowing for a streamlined development process and robust data management.

![Entity Relationship Diagram ERD](documentation/readme_photos/erd.png)

### Models

#### AddCategory model

**The AddCategory model** is used to categorize various entries in the application. It contains the following fields:

- category_id: Auto-incremented primary key.
- category_name: Name of the category (e.g., Routines, Podcasts, Indoor activities, Outdoor activities).
- user: Foreign key linking to the user who created the category.
 -created_on: Date and time when the category was created.

The predefined categories are:
- Routines
- Podcasts
- Indoor activities
- Outdoor activities

These categories can only be added by the admin user in the admin panel to ensure all activities are categorized correctly.

### Agile Methodologies

#### Epics

#### User stories

#### MoSCoW prioritization

#### Kanban board

### Technologies Used

#### Languages

#### Frameworks

#### Libraries

#### Tools & Programs

### Testing

[Testing](testing.md) 

### Deployment

#### GitHub

#### Heroku

### Features

### Credits

#### Code

#### Media

#### Acknowledgements