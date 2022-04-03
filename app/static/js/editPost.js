const updatePost = async (e) => {
    e.preventDefault()
    const newTitleInput = document.querySelector('#editPostTitle').value.trim();
    const newContentInput = document.querySelector('#editPostContent').value.trim();
    const postID = window.location.pathname.split('/').pop();
    const userID = document.querySelector('#welcomeName').getAttribute('data-user-id');
    
    const response = await fetch(`/api/posts/${postID}`, {
        method: 'PUT',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify({
            title: newTitleInput,
            description: newContentInput,
            user_id: userID,
        })
    });
    if (response.ok) {
        window.location.assign('/dashboard');
    } else {
        alert('unable to update post');
    };
};

document.querySelector('#updatePostButton').addEventListener('click', updatePost);