const createPost = async (e) => {
    e.preventDefault();
    const titleInput = document.querySelector('#newPostTitle').value.trim();
    const contentInput = document.querySelector('#newPostContent').value.trim();
    const userID = document.querySelector('#welcomeName').getAttribute('data-user-id');
    const response = await fetch('/api/posts', {
        method: 'POST',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify({
            description: contentInput,
            title: titleInput,
            user_id: userID,
        })
    });
    if(response.ok) {
        window.location.assign('/dashboard');
    } else {
        alert('Cannot create post');
    }
}

document.querySelector('#submitPostButton').addEventListener('click', createPost);