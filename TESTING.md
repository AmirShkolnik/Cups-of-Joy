# Cup Of Joy | Testing

Back to the [README.md](/workspace/job-finder/README.md)

We tested this webpage very carefully many times while we were making it. We did this testing to make sure all the different parts and features work smoothly and properly.

## Manual Testing

### As a visitor

| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
### Navbar
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Links - Click to open links | Redirect to each page | Passed |
| Logo - Click on the Logo | Redirect to the home page | Passed|
| Register - Click on the "Register" Button | Redirect to the relevant pages | Passed |
| Login - Click on the "Login" Button | Redirect to the relevant pages | Passed |
| Logout - Click on the "Logout" Button | Redirect to the relevant pages | Passed |
### Home - Fisrt LP Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Click on the clickable "Login" box | Redirect to the relevant pages | Passed|
| Click on the clickable "Coffee Shops Reviews" box | Redirect to the relevant pages | Passed|
| Click on the clickable "Articles" box| Redirect to the relevant pages | Passed|
| Click on the clickable "Home" box | Redirect to the relevant pages | Passed|
### Articles List Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Navbar - Click on Articles | Redirect to the correct Articles list with with images, text, author and date | Passed |
| Click on the "next" or "back" buttons below the articles | Redirect to the next/prev page | Passed |
| Click on an Article from Articles page | Redirect to the correct Article | Passed |
| Likes - Heart icon and numbers | Should display - NOT clickable | Passed |
| Date - Article published date | Should display | Passed |
### Singel Article Page 
| What was tested | Expected Result | Outcome |
|:---|:---|:---:| 
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
|:---|:---|:---:|
| Navbar - Click on "Reviews" button | Redirect to the Reviews page | Passed |
| No Reviews | Show a message "There are no reviews yet. Please log in or register to add a review." bg image | Passed |
| Reviews Page - Empty - Click on the "lon in" link| Redirect to accounts/login/ | Passed |
| Reviews Page - Empty - Click on the "register" link| Redirect to accounts/signup/ | Passed |
| Reviews Page - Atleast one review | Redirect to the correct reviews list with images, text, author and date| Passed |
| Reviews Page - Atleast one review | Slideshow above reviews list with rotating, fading images | Passed |
| Reviews Page - Atleast one review | Clickable dots under slideshow | Passed |
### Singel Review Page 
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Review - Click on a Review from Reviews list page | Redirect to the correct Review page | Passed |
| Review - Written by Author and published date | Should display | Passed |
| Review status| Should NOT display | Passed |
### Register - Sign Up Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Navbar - Click on Register | Redirect to Sign Up page | Passed |
| Creating an account | Username and Password are required | Passed |
| Password | Auto password creation | Passed |
| Email| Email address is only optional to create an account | Passed |
| After Sign Up| Redirect to Articles page and success message is prompt| Passed |
### Login - Sign In Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Navbar - Click on Login | Redirect to Login page - accounts/login | Passed |
| Sign In | Username and Password are required, remember me is optional | Passed |
| Sign In with wrong name or password | Warning message - The username and/or password you specified are not correct | Passed |
| Register link | Redirect to the correct Page | Passed |
### Footer
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Social Media  Buttons- Click on the social media links in the footer | Redirects to the relevant social media page in a new tab | Passed |
| About Us - Click | Redirect to about/ | Passed |
| Coffee Shops Reviews - Click | Redirect to coffeeshop/index | Passed |
| For Coffee Lovers - Click | Redirect to home page - blog/index | Passed |
### As a logged in User 
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Login - Click on the "Sign in" button | Message should prompt "Successfully signed in as user." | Passed |
| Click on the "User Name" button | Display dropdown menu | Passed |
### My Reviews Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Dropdown Menu - Click on the "My Reviews" link | Redirect to coffeeshop/add_review | Passed |
| Dropdown Menu - Click on the "My Reviews" link | If the user wrote a review it should display | Passed |
| Dropdown Menu - Click on the "My Reviews" link | If the user didn't write a review it should display "You haven't added any reviews yet." | Passed |
| Click on the "My Reviews" link | click on "Add Review" button redirect to coffeeshop/add | Passed |
| Single Review | Should display 3 buttons - View, Edit, Delete | Passed |
### Single Review Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| View - Single Review - click View | Should redirect to the single review page | Passed |
| View - Single Review - click View | Should display, image, text, author and review status - limited for user only | Passed |
| Edit - Single Review - click Edit | Should redirect to the single review edit page | Passed |
| Delete - Single Review - click Delete | Should redirect to coffeeshop/delete/review-id-number for confirmation | Passed |
### My Favourites Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Dropdown Menu - Click on the "My Favourites" link | Redirect to blog/favourites/ | Passed |
| Dropdown Menu - Click on the "My Favourites" link | If the user didn't save any Favourites it should display "You don't have any favorites yet." | Passed |
| Remove - Click on the "Remove" button | Should redirect to favourite/article-name/remove/ | Passed |
### My Comments Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Dropdown Menu - Click on the "My Comments" link | Redirect to blog/comments/ | Passed |
| Dropdown Menu - Click on the "My Comments" link | Should display article headline, comment and published date | Passed |
| Click on the "My Comments" link | Headline should be clickable | Passed |
### Singel Article Page
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
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
|:---|:---|:---:|
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
|:---|:---|:---:|
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
### About Us
| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Contact form submitted | Notification: "We got your message! We endeavor to respond within 2 working days." | Passed |
| Click Submit - missing fields | Notification: "Fill this field." | Passed |

### Notifications and Errors

| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
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

### Layout and built in functionality

| What was tested | Expected Result | Outcome |
|:---|:---|:---:|
| Recipe posts | Views as newest recipes to oldest on the home page | Passed |
| Time stamps on recipes and comments | Views the time a post or comment is created | Passed |
| "Like" icon on home page | "Like" icon and count updates on home page | Passed |
| Comment counter | Displays the correct number of comments | Passed |
| Author banner on the recipe post | Displays the correct author | Passed |
| Recipe titles cannot be duplicated | A recipe wont allow posting if another one exist with the same title | Passed |

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

Some html pages do contain comments for ease of navigation through sections

<details>
<summary> First html validator test - FIXED
</summary>

![html error](./assets/docs/html-error.png)

</details>

- Error: Element p not allowed as child of element span - Fixed

<details>
<summary> Second html validator test
</summary>

![html error](./assets/docs/html-no-errors.png)

</details>

- No errors and no warnings were found on the second test

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

<details>
<summary> CSS validator test
</summary>

![html error](./assets/docs/css-validator.png)

</details>

- No errors were found but warnings due to webkits are noted

### [JSHint JavaScript Validator](https://jshint.com/)

<details>
<summary> JSHint JavaScript Validator
</summary>

![html error](./assets/docs/js-validator.png)

</details>

- No errors were found

### [CI Python Linter](https://jshint.com/)

<details>
<summary> CI Python Linter
</summary>

![CI Python Linter](./assets/docs/python-validator.png)

</details>

- All Python files were tested, no errors or warnings were found. An example on the views.py file can be seen.


## Fixed Bugs

1. Slug field was added to the Recipe model after the model was created however it was creating errors. The fix was to provide a default value of null.
2. Text fields for the parts Recipe post form however they did not allow for user editing, summernote was added to create a better user experience when adding recipe ingredients & Instructions
3. The summernote editors were not responsive on smaller devices credits to my husband and fellow student who found a way to customise summernote editor in the settings.py file.
4. Other bugs were minor spacing and colour matching of buttons, layouts etc that had been fixed.
5. Summernote in the admin panel on some fields had disappeared after adding summernote configuration to settings.py. The fix was done by removing the iframes=false config.

## Known / Unresolved Bugs

1. The Recipe posts on the home page are slightly big on the desktop view, so I have considered adding more recipes to the first page to give it a more squashed view. 
2. Comments get duplicated if a user refreshes their web page after posting a comment on a recipe post.
3. List style on Recipe posts ingredients looks great with the bullet point in more views however does not work well when using devices 500px and smaller.
4. The recipe post image, excerpt, cook & prep time and serves fields are not fitting to my liking on mobile screen sizes. This will be fixed after some research and changes have been done.

Back to the [README.md](https://github.com/NicoleJackson89/pp4-recipe-share/blob/main/TESTING.md)