import React, { useRef, useState,useEffect} from 'react';
import '../styles/style.css';
import { Icon } from 'semantic-ui-react';



function ImageSlider(){

   // We use the useRef hook to get a reference to the slider container
   const sliderRef = useRef(null);
   const [scrollAmount,setScrollAmount] = useState(0); // The amount to scroll when clicking the navigation buttons
   const [images, setImages] = useState([
    // Here, you can add your own image objects with their respective URLs
    { id: 1, url: 'https://as1.ftcdn.net/v2/jpg/02/84/08/56/1000_F_284085674_vaA15KXbtnnVxHVbBkTqMwMA1R6cYqNJ.jpg' },
    { id: 2, url: 'https://as2.ftcdn.net/v2/jpg/02/79/66/33/1000_F_279663378_b6mTMZYfRBZCoqrIR4rFxFcRf7hyTALu.jpg' },
    { id: 3, url: 'https://as1.ftcdn.net/v2/jpg/02/67/10/42/1000_F_267104237_qWXZTQQnSDU7ubLs0spoB2cYSFs1vA5b.jpg' },
    { id: 4, url: 'https://as2.ftcdn.net/v2/jpg/04/70/44/63/1000_F_470446341_ImTU6thIoFkkKTTf3ozJIi60BxKXqXXk.jpg' },
    { id: 5, url: 'https://as1.ftcdn.net/v2/jpg/02/20/16/44/1000_F_220164473_VVsYP7fssuwdi2Lxi3LeoGe74ZQTkgW5.jpg' },
   ]);

   // scrolling one image over
   useEffect(() => {
    if (sliderRef.current && sliderRef.current.firstChild) {
      //set scroll amount to width of first image
      setScrollAmount(sliderRef.current.firstChild.offsetWidth);
    }
   },[]);

 // image slider compenent render
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
     <Icon name="chevron left"/>
  </button>
  {/* Image container */}
  <div className="images-container" ref={sliderRef}>
    {images.map((image) => (
        <img
        className="sliderimage"
        alt="sliderImage"
        key={image.id}
        src={image.url}
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
        <Icon name="chevron right" />
      </button>
   </div>
 );
}
export default ImageSlider;