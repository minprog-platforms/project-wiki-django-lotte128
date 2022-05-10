# Wiki

## Description
This app allows users to read and add encyclopedia entries in app. Each entry is presented at it's own page. With the search function, users can search for entries in app.

## Requirements
![Workflow sketch](/wiki_images/workflow.jpg)

### Entry Page
Displays content of encyclopedia entry.
![Entry Page sketch](/wiki_images/entry_page.jpg)
- Title of the page must include the name of the entry.
- If the page exists, the user is presented with a page that displays the content of the entry
- If the page doesn't exist, the user is presented with an error: "requested page not found".

### Index Page
Lists names of all pages in the encyclopedia.
![Index Page sketch](/wiki_images/index_page.jpg)
- User can click on any entry to be taken tot that page.

### Search function
- Box in the sidebar to search for an entry.
- If the query matches name of an entry, user is taken to that page.
- If query doesn't match, user is taken to search results page with list of all entries that have query as a substring.
    - User can click on result to go to entry page.

### Substring page
- Page user is taken to with list of entries that have
query as substring.

### New Page
Clicking "Create New Page" takes user to page where they can create a new entry.
![New Page sketch](/wiki_images/create_new_page.jpg)
- Users can enter title
    - In a textarea, users can add Markdown content for page.
- Click button to save new page.
- Entry is saved to disk.
    - User is taken to new page.
- If entry already exists with provided title, user gets error message.
