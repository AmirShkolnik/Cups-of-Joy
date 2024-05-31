# Testing

During the creation of CupsofJoy, thorough testing was done to make sure each new feature worked properly before adding it to the main version of the website.

Different tests were sent to new users to try out. The goal was to get feedback from a variety of users on different devices and web browsers. This helped identify and fix any problems while the website was still being built.


This is the TESTING file for the [CupsOfJoy](https://cupsofjoy-c2c917eb3f59.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing  Table of Contents  
- [Testing](#testing)
  - [Testing Table of Contents](#testing--table-of-contents)
  - [Manual Testing](#manual-testing)
      - [As a visitor](#as-a-visitor)
      	- [Navbar](#navbar)
        - [Home](#home)
	- [Articles List Page](#articles-list-page)
        - [Reviews List Page](#reviews-list-page)
        - [Singel Review Page](#singel-review-page)
    	- [Sign Up Page](#sign-up-page)
        - [Sign In Page](#sign-in-page)
	- [Footer](#footer)
        - [Reviews List Page](#reviews-list-page)
        - [Singel Review Page](#singel-review-page)
	- [About Us](#about-us)
     - [As a logged in User](#as-a-logged-in-user)
      	- [My Reviews Page](#my-reviews-page)
        - [Single Review Page](#single-review-page)
	- [My Favourites Page](#my-favourites-page)
        - [My Comments Page](#my-comments-page)
        - [Singel Article Page](#singel-article-page)
    	- [Add New Review](#add-new-review)
        - [Edit a Review](#edit-a-review)
     - [Notifications and Errors](#notifications-and-errors)
     - [Layout and Built in Functionality](#Layout-and-built-in-functionality)
  - [Chrome Developer Tools](#chrome-developer-tools)
  - [Browser Testing](#browser-testing)
  - [Validation](#validation)
      - [HTML Validation](#html-validation)
      - [CSS Validation](#css-validation)
      - [JavaScript Validation](#javascript-validation)
      - [Python Validation](#python-validation)
      - [Lighthouse Scores](#lighthouse-scores)
      - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Django Messages Implementation Testing](#django-messages-implementation-testing)
    - [User Story Testing](#user-story-testing)
    - [Responsiveness - Dev Tools/Real World Device Testing](#responsiveness---dev-toolsreal-world-device-testing)
  - [Automated Testing](#automated-testing)
    - [Running the Tests](#running-the-tests)
    - [Test Database](#test-database)
    - [Importance of Testing](#importance-of-testing)
    - [Continuous Integration](#continuous-integration)
  - [Bugs](#bugs)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
    - [Unknown Bugs](#unknown-bugs)


# Testing

Back to the [README.md](/workspace/job-finder/README.md)

We tested this webpage very carefully many times while we were making it. We did this testing to make sure all the different parts and features work smoothly and properly.

## Manual Testing

### As a visitor

### Navbar

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Links - Click to open links | Redirect to each page | Passed |
| Logo - Click on the Logo | Redirect to the home page | Passed|
| Register - Click on the "Register" Button | Redirect to the relevant pages | Passed |
| Login - Click on the "Login" Button | Redirect to the relevant pages | Passed |
| Logout - Click on the "Logout" Button | Redirect to the relevant pages | Passed |

### Home

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Click on the clickable "Login" box | Redirect to the relevant pages | Passed|
| Click on the clickable "Coffee Shops Reviews" box | Redirect to the relevant pages | Passed|
| Click on the clickable "Articles" box| Redirect to the relevant pages | Passed|
| Click on the clickable "Home" box | Redirect to the relevant pages | Passed|

### Articles List Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Navbar - Click on Articles | Redirect to the correct Articles list with with images, text, author and date | Passed |
| Click on the "next" or "back" buttons below the articles | Redirect to the next/prev page | Passed |
| Click on an Article from Articles page | Redirect to the correct Article | Passed |
| Likes - Heart icon and numbers | Should display - NOT clickable | Passed |
| Date - Article published date | Should display | Passed |

### Singel Article Page 

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Written by Author and published date | Should display | Passed |
| Likes - Click on the "Like" button | No action should take place | Passed |
| Likes - Heart icon and numbers | Should display | Passed |
| Likes - Message "Please log in to like and add to favorites." | Should display | Passed |
| Comments - Click on the "Comment" button | No action should take place | Passed |
| Comments - comments icon and numbers | Should display | Passed |
| Comments - Comments and published date | Should display at the end of the article | Passed |
| Comments - Message "Log in to leave a comment" | Should display at the end of the article | Passed |

### Reviews List Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Navbar - Click on "Reviews" button | Redirect to the Reviews page | Passed |
| No Reviews | Show a message "There are no reviews yet. Please log in or register to add a review." bg image | Passed |
| Reviews Page - Empty - Click on the "lon in" link| Redirect to accounts/login/ | Passed |
| Reviews Page - Empty - Click on the "register" link| Redirect to accounts/signup/ | Passed |
| Reviews Page - Atleast one review | Redirect to the correct reviews list with images, text, author and date| Passed |
| Reviews Page - Atleast one review | Slideshow above reviews list with rotating, fading images | Passed |
| Reviews Page - Atleast one review | Clickable dots under slideshow | Passed |

### Singel Review Page 

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Review - Click on a Review from Reviews list page | Redirect to the correct Review page | Passed |
| Review - Written by Author and published date | Should display | Passed |
| Review status| Should NOT display | Passed |

### Sign Up Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Navbar - Click on Register | Redirect to Sign Up page | Passed |
| Creating an account | Username and Password are required | Passed |
| Password | Auto password creation | Passed |
| Email| Email address is only optional to create an account | Passed |
| After Sign Up| Redirect to Articles page and success message is prompt| Passed |

### Sign In Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Navbar - Click on Login | Redirect to Login page - accounts/login | Passed |
| Sign In | Username and Password are required, remember me is optional | Passed |
| Sign In with wrong name or password | Warning message - The username and/or password you specified are not correct | Passed |
| Register link | Redirect to the correct Page | Passed |

### Footer

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Social Media  Buttons- Click on the social media links in the footer | Redirects to the relevant social media page in a new tab | Passed |
| About Us - Click | Redirect to about/ | Passed |
| Coffee Shops Reviews - Click | Redirect to coffeeshop/index | Passed |
| For Coffee Lovers - Click | Redirect to home page - blog/index | Passed |

### About Us

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Contact form submitted | Notification: "We got your message! We endeavor to respond within 2 working days." | Passed |
| Click Submit - missing fields | Notification: "Fill this field." | Passed |

### As a logged in User 

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Login - Click on the "Sign in" button | Message should prompt "Successfully signed in as user." | Passed |
| Click on the "User Name" button | Display dropdown menu | Passed |

### My Reviews Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Dropdown Menu - Click on the "My Reviews" link | Redirect to coffeeshop/add_review | Passed |
| Dropdown Menu - Click on the "My Reviews" link | If the user wrote a review it should display | Passed |
| Dropdown Menu - Click on the "My Reviews" link | If the user didn't write a review it should display "You haven't added any reviews yet." | Passed |
| Click on the "My Reviews" link | click on "Add Review" button redirect to coffeeshop/add | Passed |
| Single Review | Should display 3 buttons - View, Edit, Delete | Passed |

### Single Review Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| View - Single Review - click View | Should redirect to the single review page | Passed |
| View - Single Review - click View | Should display, image, text, author and review status - limited for user only | Passed |
| Edit - Single Review - click Edit | Should redirect to the single review edit page | Passed |
| Delete - Single Review - click Delete | Should redirect to coffeeshop/delete/review-id-number for confirmation | Passed |

### My Favourites Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Dropdown Menu - Click on the "My Favourites" link | Redirect to blog/favourites/ | Passed |
| Dropdown Menu - Click on the "My Favourites" link | If the user didn't save any Favourites it should display "You don't have any favorites yet." | Passed |
| Remove - Click on the "Remove" button | Should redirect to favourite/article-name/remove/ | Passed |

### My Comments Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Dropdown Menu - Click on the "My Comments" link | Redirect to blog/comments/ | Passed |
| Dropdown Menu - Click on the "My Comments" link | Should display article headline, comment and published date | Passed |
| Click on the "My Comments" link | Headline should be clickable | Passed |

### Singel Article Page

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Add Like - Click on the "Like" heart icon | Add 1 to the number of likes and the heart turns red, green message "Added to likes." | Passed |
| Remove Like - Click on the "Like" heart icon | Should redirect to like/article-slug/confirm/ | Passed |
| Remove Like - Click on the "Cancel" button | Should redirect back to the article | Passed |
| Remove Like - Click on the "Confirm" button | Should redirect back to the article and dedact 1 to the number of likes and the heart turns empty | Passed |
| Comments | A body window should be active for typing | Passed |
| Comments - Click on the "Submit" button after adding a comment | A green window message should prompt "Comment submitted and awaiting approval" | Passed |
| Comments Icon after approval | Add 1 to the number of comments and the comment should display | Passed |
| Comments after approval | Delet and Edit options are available | Passed |
| Delete - Comments after approval - Click on "Delete" Button | Warning window should open with close and delete options, close - remove window and stay on page, delete - remove comment | Passed |
| Edit - Comments after approval - Click on "Edit" Button | comment display on window and an "Update" button display. After updating a message should display - "Comment updated and is awaiting approval." | Passed |
| Add to Favourites - Click on the "Bookmark" icon | Icon should turns red and a green message display "Added to favorites." | Passed |
| Remove from Favourites - Click on the "Bookmark" icon | Should redirect to favourite/article-name/remove/ with 2 optins Confirm and Cancel, Cancel redirect back to the article, Confirm remove from favourites and redirect back to the article. Green message display "Removed from favorites." | Passed |

### Add New Review

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Dropdown Menu - Click on the "Add New Review" link | Redirect to coffeeshop/add | Passed |
| Populated all the fields in the add a review detail page, click on the "Add Review" button| User is redirected to coffeeshop/add_review/ reviews list page | Passed |
| Cancel - click on the "Cancel" button at any stage | Javascript message prompt, asking the user to confirm canceling, display 2 message buttons - click cancle: user stay on page and no changes are lost, click ok: user redirect to coffeeshop/add_review/ - User's Reviews list page | Passed |
| Check box - unchecked | "Request Approval" button NOT clickable, button's color is off | Passed |
| Check box - checked | "Request Approval" button IS clickable, button's color is green. After click the user is redirected to coffeeshop/add_review - User's Reviews list page, Green message prompt "Review added successfully, waiting for approval." and display "This review is in draft status." under article headline | Passed |
| Missing or unvalid fileds - Click on the "Request Approval" button | Warning disply "Please fill in all required fields." relevant field is marked with text. | Passed |
| No image uploaded | Display default coffee image | Passed |
| Status - Draft | New Review is added at the Admin back office for approval with status draft, display "This review is in draft status." under article headline  | Passed |
| Status - Admin approved- User - Draft | On coffeeshop/add_review/ under the headline the text should display "Your review has been approved. Click the Edit button to change the status to Published." | Passed |
| Status - Admin approved- User - published | Display "Status: This review is published." under article headline. | Passed |
| Status - Admin not approvd YET- User - published | Display "Status: This review is awaiting approval." under article headline. | Passed |
| Status - Admin Rejected | Display "Status: This review got rejected, please follow our guidelines" under article headline. | Future Feature |

### Edit a Review 

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| coffeeshop/add_review/ - Click on the "Edit" button | Redirect to coffeeshop/edit/review-number | Passed |
| Edit relevant fields, check the box and click on the "Save Changes" button| User is redirected to coffeeshop/relevant-review, image, status, author and contnet should display, Green message "Review Update" display | Passed |
| Cancel - click on the "Discard Changes" button at any stage | Javascript message prompt, asking the user to confirm canceling, display 2 message buttons - click cancle: user stay on page and no changes are lost, click ok: user redirect to coffeeshop/add_review/ - User's Reviews list page | Passed |
| Check box - unchecked | "Request Approval" button NOT clickable, button's color is off | Passed |
| Check box - checked | "Request Approval" button IS clickable, button's color is green. After click 
the user is redirected to coffeeshop/relevant-review, Green message prompt "Review updated." and display "Status: This review is awaiting approval." under article headline | Passed |
| Missing or unvalid fileds - Click on the "Request Approval" button | Warning disply "Please fill in all required fields." relevant field is marked with text. | Passed |
| No image uploaded | Display default coffee image | Passed |
| Edit Status to Draft | Review's status has been changed at the Admin back office for approval with status draft, display "This review is awaiting approval." under article headline both on the review and reviews list page | Passed |
| Status - Admin approved- User - published | Display "Status: This review is published." under article headline. | Passed |

### Notifications and Errors

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Login | Notification: "Successfully signed in as {username}." | Passed |
| Logout | Notification: "You have signed out." | Passed |
| Register - Sign-up | Notification: "Successfully signed in as {username}." | Passed |
|User's Review Administration Page| Empty: Notification - "You haven't added any reviews yet." | Passed |
| Review created & submitted | Notification: "Review added successfully, waiting for approval." | Passed |
| Review edited & submitted | Notification: "Review updated.", "Status: This review is in xxx status." Author name. | Passed |
| Delete a Review confirmation | Notification: "Are you sure you want to delete "title"?" | Passed |
| Delete a Review | Notification: "Review deleted successfully." | Passed |
| My favourite posts page | Empty: "You don't have any favorites yet." | Passed |
| Add favourite posts | Notification: "Added to favorites." | Passed |
| Add favourite posts | Notification: "red bookmark sign" | Passed |
| Remove favourite posts confirmation | Notification: "Are you sure you want to remove "title" from your favorites?" | Passed |
| Remove favourite posts | Notification: "Removed from favorites." | Passed |
| Add likes | Notification: "Added to likes." | Passed |
| Likes counter | Displays the correct number of likes | Passed |
| Remove likes confirmation | Notification: "Are you sure you want to remove "Title" from your likes?" | Passed |
| Remove likes | Notification: "Removed from likes." | Passed |
| My comments page | Empty: "You haven't made any comments yet." | Passed |
| Post a comment | Notification: "Comment submitted and awaiting approval" | Passed |
| Comment counter| Displays the correct number of comments | Passed |
| Update a comment | Notification: "Comment updated and is awaiting approval." | Passed |
| Delete a comment confirmation | Notification: "Are you sure you want to delete your comment? This action cannot be undone." | Passed |
| Delete a comment | Notification: "Comment deleted!" | Passed |
| Contact form submitted | Notification: "We got your message! We endeavor to respond within 2 working days." | Passed |
| Appending a page url to the search bar that does not exist  | Redirect to 404 - PAGE NOT FOUND | Passed |

### Layout and Built in Functionality

| What was tested | Expected Result | Outcome |
|------------------------------|--------------------------------------|--------|
| Home | Background image with interactice navigation with the user name after login | Passed |
| Articles | Views as newest articles to oldest on the articles page | Passed |
| Time stamps on articles, reviews and comments | Views the time a post or comment is created | Passed |
| Author name on articles, reviews and comments | Views the time a post or comment is created | Passed |
| "Like" icon on articles page | "Like" icon and count updates on articles page | Passed |
| "Like" icon on single article page | "Like" icon and count updates on article page | Passed |
| Likes counter | Displays the correct number of likes | Passed |
| "Favourite" icon on single article page | "Favourite" icon on article page | Passed |
| Comment counter | Displays the correct number of comments | Passed |
| Author banner on the article post | Displays the correct author on the articles list page | Passed |
| Rotating slideshow with navigation dots | Displays fading images automaticly | Passed |
| Rotating slideshow with navigation dots | Clickable dots in sync with images | Passed |
| Empty reviews page | when there are no reviews "Be the first" page is display | Passed |
| Transparnt Navbar and Footer | Display on home page| Passed |

### Chrome Developer Tools

Chrome developer tools were used throughout the development of the webpage to test responsiveness. Responsiveness was tested using developer Tools to emulate the following devices:
- Desktop 
- Laptops
- Tablets
- Mobile phones

### Browser Testing

During the development of the webpage the testing was done using Google Chrome. In production the site has been tested on the following browsers:
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Opera

## Validation

### [W3C HTML Validator](https://validator.w3.org/)

### HTML Validation
- **Tool Used:** [HTML W3C Markup Validator](https://validator.w3.org/)
- **Purpose:** It checks the application's HTML code to make sure it has no writing mistakes and follows the rules made by the World Wide Web Consortium (W3C).
- **Process:** Every web page of the Software Stacks website is checked using the W3C validator tool. This tool helps identify and fix any errors or warnings in the HTML code.

**HTML Validation Results**

The table below shows the results of checking the HTML code for different pages of the Software Stacks website. This check makes sure the HTML follows the proper rules and standards. Following these rules helps the website work well on different web browsers and also helps search engines find the website more easily.

| HTML Source Code/Page        | Validation Results PDF                | Errors | Warnings |
|------------------------------|---------------------------------------|--------|----------|
| **Home Page**                | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/home.pdf) | 0      | 0        |
| **About & Contact Page**     | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/about.pdf) | 0      | 0        |
| **Articles Page**            | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/articles.pdf) | 0      | 0        |
| **Reviews Page**             | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/reviews.pdf) | 0      | 0        |
| **Register Page**            | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/register.pdf) | 0      | 0        |
| **Login Page**               | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/login.pdf) | 0      | 0        |
| **My Reviews Page**          | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/my-reviews.pdf) | 0      | 0        |
| **Add New Review**           | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/add-new-review.pdf) | 11      | 0        |
| **Edit A Review**           | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/edit-a-review.pdf) | 11     | 0        |
| **My Favourites Posts**      | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/my-favourites.pdf) | 0      | 0        |
| **My Comments**              | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/my-comments.pdf) | 0      | 0        |
| **Logout Page**              | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/sign-out.pdf) | 0      | 0        |
| **Single Review Page**       | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/single-review.pdf) | 0      | 0        |
| **Single Article Page**      | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/single-article.pdf) | 0      | 0        |
| **My Favourites Page**        | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/my-favourites.pdf) | 0      | 0        |
| **My Comments Page**         | [View PDF](https://github.com/AmirShkolnik/Cups-of-Joy/blob/main/documentation/html-validation-pdf/my-comments.pdf) | 0      | 0        |
| **404 Page**                 | [View PDF](documentation/html-validation-pdf/404.pdf) | 0      | 0        |

### CSS Validation
- **Tool Used:** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- **Purpose:** Checks that the CSS code used on the website follows the rules set by the W3C and does not contain any mistakes.
- **Process:** The CSS files (which control the styling and layout of the website) are checked using the W3C CSS Validator tool. Any issues or problems found are then fixed. Making these fixes helps the website look and work better on different web browsers.
<details>
<summary> CSS validator test
</summary>

![html error](documentation/css-validator-images/css.png)

</details>

- No errors were found but warnings due to webkits are noted

### [JSHint JavaScript Validator](https://jshint.com/)

<details>
<summary> Add A Review Page - Checkbox JavaScript Validator
</summary>
![add checkbox](documentation/js-validator-images/add - checkbox.png)
</details>

<details>
<summary> Edit A Review Page - Checkbox JavaScript Validator
</summary>
![edit checkbox](documentation/js-validator-images/edit - checkbox.png)
</details>

<details>
<summary> Comments JavaScript Validator
</summary>
![comments](documentation/js-validator-images/comments.png)
</details>

<details>
<summary> Reviews Page - Slideshow JavaScript Validator
</summary>
![slideshow](documentation/js-validator-images/slideshow.png)
</details>

### JavaScript Validation
- **Tool Used:** [JSLint/JSHint](https://jshint.com/)
- **Purpose:** To find mistakes and possible issues in the JavaScript code, making sure that all the scripts work properly and do not have any errors.
- **Process:** The JavaScript code is checked by special tools called JSLint and JSHint. These tools look for mistakes in the way the code is written, find any outdated methods being used, and point out parts of the code that could be improved to work better.

Below is a table summarizing the JavaScript validation results for specific files within the Software Stacks website. 

| JavaScript File              | Results Screenshots               | Errors | Warnings |
|------------------------------|--------------------------------------|--------|----------|
| **comments.js**                  | ![screenshot](documentation/js-validator-images/comments.png)  | 0      | 19      |
| **slideshow**            | ![screenshot](documentation/js-validator-images/slideshow.png) | 0  | 10       |
| **add review**         | ![screenshot](documentation/js-validator-images/add-checkbox.png) | 0 | 3       |
| **edit review**         | ![screenshot](documentation/js-validator-images/edit-checkbox.png) | 0 | 3        |

- No errors were found

### Python Validation
- **Tool Used:** [CI Python Linter](https://pep8ci.herokuapp.com/#)
- **Purpose:** Checks the Python code to find any mistakes, make sure it follows a set of coding rules, and look for parts of the code that could be improved or written in a better way."
- **Process:** The Python code used in Cups Of Joy is checked with a tool called Pylint. This tool makes sure the code follows the correct rules and standards for writing good quality code.

**Cups of Joy - Project Module Python Validation Results**
| Python File   | Results Screenshots                        | Errors | Warnings |
|----------------------------|--------------------------------------------|--------|----------|
| **settings.py**            | ![screenshot](documentation/py-validation-images/cupsofjoy/settings.py.png) | 0      | 0        |
| **manage.py**            | ![screenshot](documentation/py-validation-images/cupsofjoy/manage.py.png) | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/py-validation-images/cupsofjoy/urls.py.png)     | 0      | 0        |
| **views.py**                | ![screenshot](documentation/py-validation-images/cupsofjoy/views.py.png)     | 0      | 0        |
| **wsgi.py**                | ![screenshot](documentation/py-validation-images/cupsofjoy/wsgi.py.png)     | 0      | 0        |
| **asgi.py**                | ![screenshot](documentation/py-validation-images/cupsofjoy/asgi.py.png)     | 0      | 0        |

**Blog Module Python Validation Results**

| Python File                | Results Screenshots                        | Errors | Warnings |
|----------------------------|--------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/py-validation-images/blog/views.py.png)   | 0      | 0        |
| **models.py**              | ![screenshot](documentation/py-validation-images/blog/models.py.png)  | 0      | 0        |
| **forms.py**               | ![screenshot](documentation/py-validation-images/blog/forms.py.png)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/py-validation-images/blog/urls.py.png)| 0      | 0        |
| **admin.py**               | ![screenshot](documentation/py-validation-images/blog/admin.py.png)   | 0      | 0       |
| **apps.py**              | ![screenshot](documentation/py-validation-images/blog/apps.py.png)  | 0      | 0        |

**Coffee Shop Module Python Validation Results**

| Python File                | Results Screenshots                        | Errors | Warnings |
|----------------------------|--------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/py-validation-images/coffeeshop/views.py.png)   | 0      | 0        |
| **models.py**              | ![screenshot](documentation/py-validation-images/coffeeshop/models.py.png)  | 0      | 0        |
| **forms.py**               | ![screenshot](documentation/py-validation-images/coffeeshop/forms.py.png)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/py-validation-images/coffeeshop/urls.py.png)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/py-validation-images/coffeeshop/admin.py.png)   | 0      | 0        |
| **apps.py**              | ![screenshot](documentation/py-validation-images/coffeeshop/apps.py.png)  | 0      | 0        |

**About Module Python Validation Results**

| Python File                | Results Screenshots                        | Errors | Warnings |
|----------------------------|--------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/py-validation-images/about/views.py.png)   | 0      | 0        |
| **models.py**              | ![screenshot](documentation/py-validation-images/about/models.py.png)  | 0      | 0        |
| **forms.py**               | ![screenshot](documentation/py-validation-images/about/forms.py.png)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/py-validation-images/about/urls.py.png)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/py-validation-images/about/admin.png)   | 0      | 0        |
| **apps.py**              | ![screenshot](documentation/py-validation-images/about/apps.py.png)  | 0      | 0        |

### Lighthouse Scores
- **Tool Used:** [Google Lighthouse](https://en.wikipedia.org/wiki/Google_Lighthouse)
- **Purpose:** To evaluate how well the web pages work in terms of speed, ease of use for people with disabilities, mobile-friendliness, ability to be found by search engines, and following recommended best practices.
- **Process:** Cups Of Joy is tested using Google Lighthouse. This tool checks how well the website performs in different areas and gives suggestions on how to make it better.

| HTML Page / Source           |     Lighthouse Report Screenshot     | 
|------------------------------|--------------------------------------|
| **Home Page**                | ![screenshot](documentation/Lighthouse/home.png) |  
| **About & Contact Page**     | ![screenshot](documentation/Lighthouse/about-us.png) | 
| **Register Page**            | ![screenshot](documentation/Lighthouse/sign-up.png) | 
| **Login Page**               | ![screenshot](documentation/Lighthouse/login.png) | 
| **Logout Page**              | ![screenshot](documentation/Lighthouse/logout.png) | 
| **Single Review**            | ![screenshot](documentation/Lighthouse/single-review.png) | 
| **Add new Review**           | ![screenshot](documentation/Lighthouse/add.png) | 
| **My Favourites Page**       | ![screenshot](documentation/Lighthouse/my-favourites.png) | 
| **My Comments Page**         | ![screenshot](documentation/Lighthouse/my-comments.png) |
| **Articles Page**            | ![screenshot](documentation/Lighthouse/articles.png) |
| **Reviews Page**            | ![screenshot](documentation/Lighthouse/reviews.png) |

## Bugs

### Solved Bugs  
  
As this was my first Django/Database project, most of the bugs that I encountered were learning and teething issues. The below bugs are bugs that I spent a longer length of time investigating or required the assistance of Tutor Support.

| No. | Bug | Solved | Fix | Solution Credit |
| --- | ---------------- | ---- | ------------- | -------------- | 
| 1   | About Us - contact form is not displaying | Yes | Adding the form rendering code in the about.html template. | CI walkthrough tutorials |
| 2   | Remove favourites from favourites list confirmation not working | Yes | Adding a new view function to handle the confirmation and removal of the favorite | CI walkthrough tutorials |
| 3   | PEP8 error - "E402 module level import not at top of file" | Yes | The error "E402 module level import not at top of file" is a style warning raised by the linter (a tool that analyzes code for potential errors or style issues). This warning occurs when import statements are not placed at the top of the file, which is the recommended practice in Python. To resolve this issue, you need to move all the import statements to the top of the file, before any other code or class definitions. | [StackOverFlow](<https://stackoverflow.com/questions/36827962/pep8-import-not-at-top-of-file-with-sys-path>) |
| 4   | PEP8 error - "E501 line too long" | Yes | The error "E501 line too long" is a style warning from the linter (a tool that analyzes code for potential errors or style issues). This warning is raised when a line of code exceeds the maximum line length, which is typically set to 79 characters for Python code. To resolve this issue, you can break the long lines into multiple lines. | [StackOverFlow](<https://stackoverflow.com/questions/53158284/python-giving-a-e501-line-too-long-error>) |
| 5   | Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (currentSlide, i) | Yes | To resolve this, I useD const instead of let for the loop variables, and create a new variable to capture the current value of i within the event listener function. | [StackOverflow](<https://stackoverflow.com/questions/46027262/functions-declared-within-loops-referencing-an-outer-scoped-variable-may-lead-to>) |
| 6   | "Imported style sheets are not checked in direct input and file upload modes" | Yes | The CSS validator I was using is not able to fetch and check the imported stylesheets from restricted URLs. Must sign in before testing.  |  |
| 7   | RuntimeError: Model class choosemug.models.Mom doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS. | Yes | After deleting the Chosemug app, I forgot to migrate.  |  |
| 8   | add_review page - Error: End tag main seen, but there were open elements. | Yes | Closing div was missing  |  |
| 9   | article page - Error: The font element is obsolete. Use CSS instead. | Yes | Add @import rules at the top of the CSS file  | [StackOverFlow](https://stackoverflow.com/questions/10036977/best-way-to-include-css-why-use-import) |

### Known Bugs

*Post Deleted Successfully!* Django message doesn't show up most of the times.

### Unknown Bugs
I am not aware of any remaining bugs.

## Known / Unresolved Bugs

1. The Recipe posts on the home page are slightly big on the desktop view, so I have considered adding more recipes to the first page to give it a more squashed view. 
2. Comments get duplicated if a user refreshes their web page after posting a comment on a recipe post.
3. List style on Recipe posts ingredients looks great with the bullet point in more views however does not work well when using devices 500px and smaller.
4. The recipe post image, excerpt, cook & prep time and serves fields are not fitting to my liking on mobile screen sizes. This will be fixed after some research and changes have been done.

Back to the [README.md](https://github.com/NicoleJackson89/pp4-recipe-share/blob/main/TESTING.md)