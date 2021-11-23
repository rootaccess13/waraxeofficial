<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">	<title>Document</title>
</head>
<style>
	.card-image{
		width: 100%;
    	height: 10vw;
    	object-fit: cover;
	}
  .viewer {
    width: 100%;
    height: 100%;

  }
  .gilid img{
    margin-top: 10px;
  }
</style>
<body>
<!-- <table class="table table-stripped" border=1 cellpadding=5 cellspacing=5 width=100% height=100%>
	<tr>
		<td><a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
		<td rowspan=3>
			<?php
				if (isset($_GET['image']))
				{
					$a=$_GET['image'];
					$b=$_GET['description'];
					print "<img src=$a width=200 height=200><br>$b";
				}
			?>
		<td><a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>


<tr>
		<td><a href='index.php?image=images/image2.png&description=robot ako1'><img src=images/image2.png width=50 height=50></a>

<tr>
		<td><a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
		<td><a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
		
<tr>
		<td><a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
		<td>
			<div class="ml-2">
			<a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
			<a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
			<a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
			<a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width=50 height=50></a>
			</div> -->
<div class="container mt-5">
  <table class="table">

      <tr>
        <th scope="col" class="text-center"><a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width="150px" height="150px"></a></th>
        <th scope="col" class="text-center"><a href='index.php?image=images/image2.png&description=robot ako'><img src=images/image2.png width="150px" height="150px"></a></th>
        <th scope="col" class="text-center"><a href='index.php?image=images/image3.png&description=robot ako'><img src=images/image3.png width="150px" height="150px"></a></th>
        <th scope="col" class="text-center"><a href='index.php?image=images/image4.png&description=robot ako'><img src=images/image5.png width="150px" height="150px"></a></th>
      </tr>


      <tr>
        <th scope="row" class="text-center">
        <a href='index.php?image=images/image8.jpg&description=robot ako'><img src=images/image8.jpg width="150px" height="150px"></a><br>
        <a href='index.php?image=images/image2.jpg&description=robot ako'><img src=images/image2.jpg  class="mt-2" width="150px" height="150px"></a>
      </th>
        <td colspan="2" class="text-center gilid">
          <?php
				if (isset($_GET['image']))
				{
					$a=$_GET['image'];
					$b=$_GET['description'];
					print "<img src=$a width=70% height=300><br>$b";
				}
			?>
        </td>
        <td class="text-center">
            <a href='index.php?image=images/image3.jpg&description=robot ako'>
            <img src=images/image3.jpg width="150px" height="150px"></a><br>
            <a href='index.php?image=images/image4.jpg&description=robot ako'>
              <img src=images/image4.jpg class="mt-2" width="150px" height="150px"></a>
        </td>

      </tr>
      <tr>
        <th scope="row" class="text-center"><a href='index.php?image=images/image1.png&description=robot ako'><img src=images/image1.png width="150px" height="150px"></a></th>
        <td class="text-center"><a href='index.php?image=images/image5.jpg&description=robot ako'><img src=images/image5.jpg width="150px" height="150px"></a></td>
        <td class="text-center"><a href='index.php?image=images/image6.jpg&description=robot ako'><img src=images/image6.jpg width="150px" height="150px"></a></td>
        <td class="text-center"><a href='index.php?image=images/image7.jpg&description=robot ako'><img src=images/image7.jpg width="150px" height="150px"></a></td>

      </tr>


  </table>
</div>
</body>
</html>
