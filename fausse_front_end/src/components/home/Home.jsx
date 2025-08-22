import React, { useState } from "react";

function Home() {
  const [email, setEmail] = useState("");

  // Updates email state
  function onChangeEmail(event) {
    setEmail(event.target.value);
  }

  function isValidEmail(emailToCheck) {
    // Regex created using Copilot and/or Windsurf VSC plug-in
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(emailToCheck);
  }
  function subscribeToNewsletter(event) {
    event.preventDefault();

    // Validate email
    if (!isValidEmail(email)) {
      console.log("That's not a valid format for an email...");
    } else {
      console.log("Subscribing...");
      document.getElementById("email").value = "";
    }
  }

  return (
    <>
      <div>
        <h1>Welcome to Café Fausse</h1>
        <p>A cousy place to spend an evening...</p>
      </div>
      <section>
        <h3>Sign up for a newsletter to not miss a thing!</h3>
        <form onSubmit={subscribeToNewsletter}>
          <input
            id="email"
            type="email"
            name="email"
            placeholder="Enter your email"
            onChange={onChangeEmail}
          />
          <button type="submit">Subscribe</button>
        </form>
      </section>
    </>
  );
}

export default Home;
