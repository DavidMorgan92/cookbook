# Testing

## Table of Contents

- [Layout](#layout)
- [Home](#home)
- [Contact](#contact)
- [Search](#search)
- [Login](#login)
- [Register](#register)
- [Account](#account)
- [Change Password](#change-password)
- [Profile](#profile)
- [Recipes](#recipes)
- [Recipe Details](#recipe-details)
- [Edit Recipe](#edit-recipe)
- [Delete Recipe](#delete-recipe)
- [Favourites](#favourites)

## Layout

### Home link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/home-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/home-link-works/after.jpg)

</details>

### Log In link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/login-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/login-link-works/after.jpg)

</details>

### Register link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/register-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/register-link-works/after.jpg)

</details>

### Contact link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/contact-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/contact-link-works/after.jpg)

</details>

### Content attribution link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/content-attribution-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/content-attribution-link-works/after.jpg)

</details>

### Favourite recipes link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/favourite-recipes-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/favourite-recipes-link-works/after.jpg)

</details>

### My recipes link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/my-recipes-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/my-recipes-link-works/after.jpg)

</details>

### My account link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/my-recipes-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/my-recipes-link-works/after.jpg)

</details>

### Log out link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/layout/log-out-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/layout/log-out-link-works/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Home

[Lighthouse Report](documentation/lighthouse-reports/home.pdf)

### Search function works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/home/search-function-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/home/search-function-works/after.jpg)

</details>

### Popular recipes are in order of most likes

<details>
<summary>Before</summary>

![Before](documentation/images/tests/home/popular-recipes-are-in-order-of-most-likes/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/home/popular-recipes-are-in-order-of-most-likes/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Contact

[Lighthouse Report](documentation/lighthouse-reports/contact.pdf)

### Message is sent by email

This was working when set up with a Gmail account. Unfortunately the account was blocked for violating Gmail's policies. I was able to set up a Postmark account using my work email which works, but the content of the email is blocked by the company policy. Therefore I've not been able to test this again.

As long as the email environment variables are set to a correct account and host then it should work.

[↑ Back to top](#testing)

## Search

[Lighthouse Report](documentation/lighthouse-reports/search.pdf)

[↑ Back to top](#testing)

## Login

[Lighthouse Report](documentation/lighthouse-reports/login.pdf)

### Login works if username and password are correct

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/login-works-if-username-and-password-are-correct/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/login-works-if-username-and-password-are-correct/after.jpg)

</details>

### Login fails if username is incorrect

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/login-fails-if-username-is-incorrect/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/login-fails-if-username-is-incorrect/after.jpg)

</details>

### Login fails if password is incorrect

<details>
<summary>Before</summary>

![Before](documentation/images/tests/login/login-fails-if-password-is-incorrect/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/login/login-fails-if-password-is-incorrect/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Register

[Lighthouse Report](documentation/lighthouse-reports/register.pdf)

### Registration succeeds if username is not taken

<details>
<summary>Before</summary>

![Before](documentation/images/tests/register/registration-succeeds-if-username-is-not-taken/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/register/registration-succeeds-if-username-is-not-taken/after.jpg)

</details>

### Registration fails if username is taken

<details>
<summary>Before</summary>

![Before](documentation/images/tests/register/registration-fails-if-username-is-taken/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/register/registration-fails-if-username-is-taken/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Account

[Lighthouse Report](documentation/lighthouse-reports/account.pdf)

### View public profile link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/account/view-public-profile-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/account/view-public-profile-link-works/after.jpg)

</details>

### Change password link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/account/change-password-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/account/change-password-link-works/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Change Password

[Lighthouse Report](documentation/lighthouse-reports/change-password.pdf)

### Change password fails if old password is incorrect

<details>
<summary>Before</summary>

![Before](documentation/images/tests/change-password/change-password-fails-if-old-password-is-incorrect/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/change-password/change-password-fails-if-old-password-is-incorrect/after.jpg)

</details>

### Change password succeeds if old password is correct

<details>
<summary>Before</summary>

![Before](documentation/images/tests/change-password/change-password-succeeds-if-old-password-is-correct/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/change-password/change-password-succeeds-if-old-password-is-correct/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Profile

[Lighthouse Report](documentation/lighthouse-reports/profile.pdf)

### Shows profile's user's recipes

<details>
<summary>Evidence</summary>

![Evidence](documentation/images/tests/profile/shows-profiles-users-recipes/evidence.jpg)

</details>

### Details links work

<details>
<summary>Before</summary>

![Before](documentation/images/tests/profile/details-links-work/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/profile/details-links-work/after.jpg)

</details>

### Profile link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/profile/profile-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/profile/profile-link-works/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Recipes

[Lighthouse Report](documentation/lighthouse-reports/recipes.pdf)

### Shows user's recipes

<details>
<summary>Evidence</summary>

![Evidence](documentation/images/tests/recipes/shows-users-recipes/evidence.jpg)

</details>

### Create link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipes/create-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipes/create-link-works/after.jpg)

</details>

### Details link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipes/details-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipes/details-link-works/after.jpg)

</details>

### Edit link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipes/edit-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipes/edit-link-works/after.jpg)

</details>

### Delete link works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipes/delete-link-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipes/delete-link-works/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Recipe Details

[Lighthouse Report](documentation/lighthouse-reports/details.pdf)

### Favourite button works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipe-details/favourite-button-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipe-details/favourite-button-works/after.jpg)

</details>

### Unfavourite button works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipe-details/unfavourite-button-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipe-details/unfavourite-button-works/after.jpg)

</details>

### Like button works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipe-details/like-button-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipe-details/like-button-works/after.jpg)

</details>

### Unlike button works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipe-details/unlike-button-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipe-details/unlike-button-works/after.jpg)

</details>

### Comment works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/recipe-details/comment-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/recipe-details/comment-works/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Edit Recipe

[Lighthouse Report](documentation/lighthouse-reports/edit.pdf)

### Change image works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/edit-recipe/change-image-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/edit-recipe/change-image-works/after.jpg)

</details>

### Remove image works

<details>
<summary>Before</summary>

![Before](documentation/images/tests/edit-recipe/remove-image-works/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/edit-recipe/remove-image-works/after.jpg)

</details>

### Doesn't allow zero ingredients

<details>
<summary>Before</summary>

![Before](documentation/images/tests/edit-recipe/doesnt-allow-zero-ingredients/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/edit-recipe/doesnt-allow-zero-ingredients/after.jpg)

</details>

### Doesn't allow zero steps

<details>
<summary>Before</summary>

![Before](documentation/images/tests/edit-recipe/doesnt-allow-zero-steps/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/edit-recipe/doesnt-allow-zero-steps/after.jpg)

</details>

### Doesn't allow serves from to be greater than serves to

<details>
<summary>Before</summary>

![Before](documentation/images/tests/edit-recipe/doesnt-allow-serves-from-to-be-greater-than-serves-to/before.jpg)

</details>

<details>
<summary>After</summary>

![After](documentation/images/tests/edit-recipe/doesnt-allow-serves-from-to-be-greater-than-serves-to/after.jpg)

</details>

<br>

[↑ Back to top](#testing)

## Delete Recipe

[Lighthouse Report](documentation/lighthouse-reports/delete.pdf)

### Delete button works

[↑ Back to top](#testing)

## Favourites

[Lighthouse Report](documentation/lighthouse-reports/favourites.pdf)

### Shows user's favourites

[↑ Back to top](#testing)
