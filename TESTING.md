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

This was working when set up with a Gmail account. Unfortunately the account was blocked for violating Gmail's policies. I was able to set up a Postmark account using my work email which works, but the content of the email is blocked by the company policy.

[↑ Back to top](#testing)

## Search

[Lighthouse Report](documentation/lighthouse-reports/search.pdf)

[↑ Back to top](#testing)

## Login

[Lighthouse Report](documentation/lighthouse-reports/login.pdf)

### Login works if username and password are correct

### Login fails if username is incorrect

### Login fails if password is incorrect

[↑ Back to top](#testing)

## Register

[Lighthouse Report](documentation/lighthouse-reports/register.pdf)

### Registration succeeds if username is not taken

### Registration fails if username is taken

[↑ Back to top](#testing)

## Account

[Lighthouse Report](documentation/lighthouse-reports/account.pdf)

### View public profile link works

### Change password link works

[↑ Back to top](#testing)

## Change Password

[Lighthouse Report](documentation/lighthouse-reports/change-password.pdf)

### Change password fails if old password is incorrect

### Change password succeeds if old password is correct

[↑ Back to top](#testing)

## Profile

[Lighthouse Report](documentation/lighthouse-reports/profile.pdf)

### Shows profile's user's recipes

### Details links work

### Profile link works

[↑ Back to top](#testing)

## Recipes

[Lighthouse Report](documentation/lighthouse-reports/recipes.pdf)

### Shows user's recipes

### Create link works

### Details link works

### Edit link works

### Delete link works

[↑ Back to top](#testing)

## Recipe Details

[Lighthouse Report](documentation/lighthouse-reports/details.pdf)

### Favourite button works

### Unfavourite button works

### Like button works

### Unlike button works

### Comment works

[↑ Back to top](#testing)

## Edit Recipe

[Lighthouse Report](documentation/lighthouse-reports/edit.pdf)

### Change image works

### Remove image works

### Doesn't allow zero ingredients

### Doesn't allow zero steps

### Doesn't allow serves from to be greater than serves to

### Doesn't allow serves to to be less than serves from

[↑ Back to top](#testing)

## Delete Recipe

[Lighthouse Report](documentation/lighthouse-reports/delete.pdf)

### Delete button works

[↑ Back to top](#testing)

## Favourites

[Lighthouse Report](documentation/lighthouse-reports/favourites.pdf)

### Shows user's favourites

[↑ Back to top](#testing)
