// Wait for the page to fully load before running the script
document.addEventListener("DOMContentLoaded", function () {
  console.log("DEBUG: ranking_update.js (v3 - Highlighting) script started!");

  // --- Get references to the HTML elements we'll need ---
  const confettiCanvas = document.getElementById("celebration-canvas");
  const celebrationAudio = document.getElementById("celebration-audio");

  // --- State Management using localStorage ---
  let previousTop3Ids =
    JSON.parse(localStorage.getItem("previousTop3Ids")) || null;
  console.log(
    "DEBUG: Loaded 'previousTop3Ids' from localStorage:",
    previousTop3Ids
  );

  // Initialize the confetti library
  const myConfetti = confetti.create(confettiCanvas, {
    resize: true,
    useWorker: true,
  });

  // --- Main Function to Fetch Rankings and Check for Changes ---
  async function checkRankingsForCelebration() {
    try {
      const response = await fetch("/api/ranking/");
      if (!response.ok) {
        return;
      }
      const participants = await response.json();

      const currentTop3Ids = participants.slice(0, 3).map((p) => p.id);

      // --- The Core Celebration Logic ---
      if (
        previousTop3Ids !== null &&
        JSON.stringify(previousTop3Ids) !== JSON.stringify(currentTop3Ids)
      ) {
        // Find the ID of the person who is in the new list but wasn't in the old one.
        const newTopper = currentTop3Ids.find(
          (id) => !previousTop3Ids.includes(id)
        );

        // If we found a new topper, celebrate them!
        if (newTopper) {
          celebrate(newTopper); // Pass the ID to the celebrate function
        }
      }

      // Save the new top 3 list to localStorage for the next page reload.
      localStorage.setItem("previousTop3Ids", JSON.stringify(currentTop3Ids));
      previousTop3Ids = currentTop3Ids;
    } catch (error) {
      console.error(
        "DEBUG: A critical error occurred while checking rankings:",
        error
      );
    }
  }

  // --- The Celebration Function (now accepts the new topper's ID) ---
  function celebrate(newTopperId) {
    console.log(
      `DEBUG: %cCELEBRATION TRIGGERED FOR PARTICIPANT ID: ${newTopperId}!`,
      "color: #FFD700; font-size: 1.5em; font-weight: bold;"
    );

    // --- NEW: HIGHLIGHT LOGIC ---
    const topperCard = document.getElementById(
      `participant-card-${newTopperId}`
    );
    if (topperCard) {
      // 1. Add the glowing class to the card
      topperCard.classList.add("new-topper-highlight");

      // 2. Set a timer to remove the class after 5 seconds (5000 milliseconds)
      setTimeout(() => {
        topperCard.classList.remove("new-topper-highlight");
        console.log(
          `DEBUG: Removed highlight from participant ID: ${newTopperId}`
        );
      }, 5000);
    }
    // --- END OF HIGHLIGHT LOGIC ---

    // Play the sound effect
    if (celebrationAudio) {
      celebrationAudio.currentTime = 0;
      celebrationAudio
        .play()
        .catch((e) => console.error("DEBUG: Audio play failed:", e));
    }

    // Fire a big, 5-second long confetti burst
    const duration = 5 * 1000;
    const animationEnd = Date.now() + duration;
    const defaults = {
      startVelocity: 30,
      spread: 360,
      ticks: 60,
      zIndex: 9999,
    };
    function randomInRange(min, max) {
      return Math.random() * (max - min) + min;
    }
    const interval = setInterval(function () {
      const timeLeft = animationEnd - Date.now();
      if (timeLeft <= 0) {
        return clearInterval(interval);
      }
      const particleCount = 50 * (timeLeft / duration);
      myConfetti(
        Object.assign({}, defaults, {
          particleCount,
          origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
        })
      );
      myConfetti(
        Object.assign({}, defaults, {
          particleCount,
          origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
        })
      );
    }, 250);
  }

  // --- Start the Process ---
  // The check will happen automatically on every page load.
  checkRankingsForCelebration();
});
