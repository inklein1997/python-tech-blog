const postComment = async (e) => {
    e.preventDefault();
    const commentInput = document.querySelector('.commentInput').value.trim();
    const postID = window.location.pathname.split('/').pop();
    const userID = document.querySelector('#welcomeName').getAttribute('data-user-id');

    if (commentInput) {
        const response = await fetch('/api/comments', {
            method: 'POST',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify({
                content: commentInput,
                post_id: postID,
                user_id: userID,
            })
        });
        if (response.ok) {
            document.location.assign(`/thread/${postID}`);
        };
    } else {
        alert('Please input a comment in the comment field before submitting')
    };
};

document.querySelector('#submitCommentButton').addEventListener('click', postComment)