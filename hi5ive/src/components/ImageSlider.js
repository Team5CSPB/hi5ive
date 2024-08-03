import React, { useRef, useState} from 'react';
import '../styles/style.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft, faChevronRight } from '@fortawesome/free-solid-svg-icons';



function ImageSlider(){

   // We use the useRef hook to get a reference to the slider container
   const sliderRef = useRef(null);
   const scrollAmount = 100; // The amount to scroll when clicking the navigation buttons
   const [images, setImages] = useState([
    // Here, you can add your own image objects with their respective URLs
    { id: 1, url: 'https://via.placeholder.com/150' },
    { id: 2, url: 'https://via.placeholder.com/150' },
    { id: 3, url: 'https://via.placeholder.com/150' },
   ]);

 // image slider compenent
 return(
 <div className="App">
  {/*Left Nav button*/}
  <button
  className="nav-btn"
  onClick={() =>{
    const container = sliderRef.current;
    container.scrollLeft -= scrollAmount; // scroll left by the specified amount
  }}
  >
     <FontAwesomeIcon icon={faChevronLeft} />
  </button>
  {/* Image container */}
  <div className="images-container" ref={sliderRef}>
    {images.map((image) => (
        <img
        className="image"
        alt="sliderImage"
        key={image?.id}
        src={image?.url}
        />
   ))}
  </div>
{/* Right navigation button */}
<button
        className="nav-btn"
        onClick={() => {
          const container = sliderRef.current;
          container.scrollLeft += scrollAmount; // Scroll right by the specified amount
        }}
      >
        <FontAwesomeIcon icon={faChevronRight} />
      </button>
   </div>
 );
}
export default ImageSlider;