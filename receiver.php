<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <title>Online Dictionary</title>

        <!-- CSS -->
        <link rel="stylesheet" href="assets//css//style.css" />

        <!-- JavaScript -->
        <script type="JavaScript" src="assets//js//#"></script>

        <!-- Website Icon -->
    </head>

    <body>
        <header>
            <h1 class="firstHeading">ONLINE DICTIONARY</h1>
        </header>

        <?php

        require 'dictionary_file.php';

        function test_input($data) {
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            $data = strtoupper($data);

            return $data;
        }

        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $searched_word = test_input($_POST["word"]);
        }

        $dictionary = dictionary();

        ?>

        <main>
            <div class="form">
                <form name="search_word" action="receiver.php" method="post">
                    <label for="word">Search Here</label><br />
                    <input type="text" name="word" id="word" placeholder="Search Your Word Here..." /><br />
                
                    <button type="submit" name="submit-btn" id="submit-btn">Submit</button>
                </form>
            </div>
            <br />
            <br />
            <br />

            <div class="definition">
                <p>
                    <span><?php echo $searched_word ?></span>: <?php echo $dictionary[$searched_word]; ?>
                </p>
            </div>
        </main>

        <footer>
                <div>
                    Click <a href="index.html">HERE</a> to return to home page
                </div>
        </footer>
    </body>
</html>