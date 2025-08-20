import React, { useState, useEffect } from "react";
import apiServices from "../../services/api_services";

function Menu() {
  const [menuItems, setMenuItems] = useState([]);

  console.log(menuItems);

  useEffect(() => {
    // fetch menu items from the back-end API '/menu'
    apiServices
      .getMenu()
      .then((response) => {
        setMenuItems(response.data.menu);
      })
      .catch((error) => console.log(`${error}`));
  }, []);

  return (
    <div>
      <h2>Menu</h2>
      {menuItems.map((item, index) => (
        <div key={index}>
          <h3>{item.name}</h3>
          <p>{item.description}</p>
          <p>Category: {item.category}</p>
          <p>Price: {item.price}</p>
        </div>
      ))}
    </div>
  );
}

export default Menu;
