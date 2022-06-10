const ReviewsList = ({ setShowModal, reviews }) => {
  let date;
  return (
    <div className="reviews-container">
      <div className="reviews-header">Reviews ({reviews.length})</div>
      <button onClick={() => setShowModal(false)} className="close-modal-btn">
        <span className="material-symbols-outlined">close</span>
      </button>
      <div className="reviews-list">
        {reviews.map((review) => {
          date = new Date(review.updated_at);
          return (
            <div key={review.id}>
              <div className="review-content">{review.content}</div>
              <div className="review-author">{review.author_name}</div>
              <div className="review-date">{date.toDateString()}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ReviewsList;
