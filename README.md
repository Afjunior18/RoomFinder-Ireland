# Planning Phase

## Strategy:

### User Research:
Ireland attracts a large number of students from all over the world, making the search for accommodation challenging. Many students cannot afford expensive student accommodations and opt for cheaper options, such as shared houses with 2, 3, 4, or sometimes more roommates. Additionally, some students prefer single rooms depending on their budget.

*Note: The user research conducted for this project was based on personal experiences, as I, as an international student, faced similar challenges upon arriving in Ireland. Most of my friends also encountered similar difficulties.*

### Competitive Analysis:
Existing platforms often facilitate accommodation searches through real estate agencies, but response times can be slow due to high demand. Moreover, Facebook communities like "Brazilian Students in Dublin" or "Venezuelan Students in Dublin" also serve as a resource, but searching can be complicated due to various posts and outdated listings. Our platform will focus solely on available rooms, removing listings once they are rented out.

*Note: The competitive analysis was also informed by personal experiences and observations, recognizing the limitations of existing platforms.*

### Feature Prioritization:
Based on user research and competitive analysis, prioritize features that address the pain points identified. Key features include:
 - User-friendly room listing creation process, allowing users offering a room to specify details like price of rent, location, description and photos.
 - Robust search and filtering options to help users find suitable accommodation quickly.
 - Secure messaging system for communication between users interested in renting or listing rooms.
 - Communication with the Post Author, details offered like, email and phone.
 - User authentication and profile management functionalities like Delete and Edit posts.
 - Admin panel for content moderation and management to ensure the platform's integrity.

### User Personas:
Develop user personas representing different segments of the target audience, such as:
- **Maria:** A budget-conscious international student looking for an affordable shared room close to her university.
- **Ahmed:** An exchange student seeking a single room with specific amenities within a reasonable budget.
- **Emily:** A local homeowner interested in renting out a spare room to international students for extra income.

*Note: The creation of user personas was influenced by personal experiences and interactions with individuals facing similar accommodation challenges.*

### Brand Identity:
RoomFinder Ireland's brand identity, which includes the logo, colour scheme, and tone of voice, is designed to connect with its users. The logo represents simplicity and trust. The font is easy to read and friendly. The tone of voice is welcoming and helpful. Consistency across the platform ensures that users always feel at ease, reinforcing the platform's values of reliability, affordability, and inclusivity.

## Scope:

RoomFinder Ireland aims to provide a user-friendly online platform for international students in Ireland to find suitable accommodation. The scope of the project includes the development of key features essential for the platform's functionality and usability:

### User Registration and Authentication:
- Users will be able to create an account, providing necessary information such as name, email, and password.

### Room Listing Creation:
- Users can list available rooms for rent, specifying details like price of rent, room type (shared or single), location, description and photos.

### Location API Integration:
- Integration of a location API to provide advanced mapping and geocoding features, allowing users to visualize the location of listed rooms and find properties based on proximity to points of interest or specific areas of the city.

### Searching and Filtering:
- Students can search for available rooms based on criteria such as location, price range and room type.

### Messaging System:
- A secure messaging system would facilitate communication between users interested in renting or listing rooms, allowing for negotiation and arrangement of terms.

### Communication with Post Author:
- Users will have access to contact information, such as email and phone number of the author of a post, enabling direct communication for further inquiries or arrangements.

### User Management:
- Users will have the ability to manage their profiles, update personal information, view their own posts, and have options to delete or edit a post if needed.

### Admin Panel:
- An admin panel will allow for content moderation, user management, and monitoring of platform activity.

- Admins will be able to approve or unapprove a post for publication.

- Admins will have the capability to delete any post if necessary.

*Additionally, features have been classified based on their importance using the MOSCOW prioritization:*

UX efforts **must** address these:
- Register and Authentication.
- Login.
- Room Listing Creation.
- Post approved/unpproved (only by admin).
- User Profile Management.

UX efforts **should have** these:
- Location API Integration.
- Room Searching and Filtering.
- Messaging System.

UX efforts **could have** these:
- Advanced Notification System: Implementation of an advanced notification system to alert users about new listings matching their preferences, updates on their inquiries, or important platform announcements.
- Social Media Integration: Integration with social media platforms to allow users to share listings or invite friends to join the platform, enhancing user engagement and expanding the platform's reach.
- Advanced Notification System: Implementation of an advanced notification system to alert users about new listings matching their preferences, updates on their inquiries, or important platform announcements.
- Review and Rating System: Incorporation of a review and rating system where users can provide feedback and rate their experiences with landlords and accommodations, helping other users make informed decisions.
- Localized Language Support: Addition of localized language support to cater to users from diverse linguistic backgrounds, providing a more inclusive experience and expanding the platform's accessibility.

## Structure
The structure of RoomFinder Ireland's platform is designed to ensure intuitive navigation and easy access to key features.

![User flow chart](docs/images/workFlow.png)

(I used [Lucidchart](https://www.lucidchart.com/) to help me visualize the user journey)

The flowchart illustrates the user journey within the platform, detailing every step from user registration to room listing creation, searching for accommodations, communication with post authors, and Admin management. Each stage is carefully mapped out to optimize user interaction and streamline the process of finding and renting accommodations

