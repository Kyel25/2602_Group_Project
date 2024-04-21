
        function applyFilters() {
            var level = document.getElementById("level-filter").value;
            var bodyPart = document.getElementById("body-part-filter").value;
            var type = document.getElementById("type-filter").value;

            // Get workout items
            var workoutItems = document.getElementsByClassName("workout-item");

            // Loop through workout items and show/hide based on filters
            for (var i = 0; i < workoutItems.length; i++) {
                var workoutItem = workoutItems[i];
                var metaText = workoutItem.querySelector(".workout-item-meta").textContent.toLowerCase();

                var showItem = true;

                // Check if workout item matches selected filters
                if (level && !metaText.includes("level: " + level.toLowerCase())) {
                    showItem = false;
                }
                if (bodyPart && !metaText.includes("body part: " + bodyPart.toLowerCase())) {
                    showItem = false;
                }
                if (type && !metaText.includes("type: " + type.toLowerCase())) {
                    showItem = false;
                }

                // Show or hide workout item based on filters
                if (showItem) {
                    workoutItem.style.display = "block";
                } else {
                    workoutItem.style.display = "none";
                }
            }
        }

        function searchWorkouts() {
            var input, filter, workoutItems, workoutTitle, i;
            input = document.getElementById("workout-search");
            filter = input.value.toLowerCase();
            workoutItems = document.getElementsByClassName("workout-item");

            for (i = 0; i < workoutItems.length; i++) {
                workoutTitle = workoutItems[i].getElementsByClassName("workout-item-title")[0];
                if (workoutTitle.textContent.toLowerCase().indexOf(filter) > -1) {
                    workoutItems[i].style.display = "block";
                } else {
                    workoutItems[i].style.display = "none";
                }
            }
        }

    