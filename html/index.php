<?php
session_start();
include ("connections/connect.php");
?>

<!doctype html>
<html lang="en-us">
<head>
<title>Rentcoach</title>
<!--Meta Tags-->
<meta charset="UTF-8">
<meta name="author" content="Rentcoach.us">
<meta name="keywords" content=""/>
<meta name="description" content="Calcula el precio ideal para alquilar tu propiedad en Barcelona. Calculadora de alquiler."/>
<!-- Set Viewport-->
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<link rel="stylesheet" href="css/bootstrap.min.css" type="text/css"/>
<link rel="stylesheet" href="css/bootstrap-theme.min.css" type="text/css"/>
<link rel="stylesheet" href="css/font-awesome.min.css">
<link rel="stylesheet" href="css/flexslider.css">
<link rel="stylesheet" href="css/select-theme-default.css">
<link rel="stylesheet" href="css/owl.carousel.css">
<link rel="stylesheet" href="css/owl.theme.css">
<link rel="stylesheet" href="css/style.css" type="text/css"/>
<!--[if IE]>
		<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->
</head>
<body id='top'>
<div class="slider-section">
	<div id="premium-bar">
		<div class="container">
			<nav class="navbar navbar-default" role="navigation">
			<div class="container-fluid">
				<!-- navegacion para movil -->
				<div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="index.html"><img src="img/logo.png" alt="logo"></a>
				</div>
				<!-- navegacion principal -->
				<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					<ul class="nav navbar-nav navbar-right">
						<li class="active"><a href="index.html">Inicio</a></li>
						<li><a href="#">Como funciona</a></li>
						<li><a href="#">Cotizar Propiedad</a></li>
						<li><a href="#">Contacto</a></li>
					</ul>
				</div>
				<!-- /.navbar-collapse -->
			</div>
			<!-- /.container-fluid -->
			</nav>
		</div>
	</div>
	<!-- Slider-Section -->
	<div class="main-flexslider">

		<ul class="slides">
			<li class='slides' id='slide-n1'><img src="img/barcelona.jpg" alt="Barcelona">
				<div class="slide-box">
					<h1>¿Cuál es el precio ideal de alquiler de tu propiedad?</h1>
					<h2>Calcula el precio ideal de tu propiedad en Barcelona.</h2>
				</div>
			</li>
		</ul>
	</div>
</div>
<!-- Calculadora de alquiler -->
<div class="search-section">
	<div class="container">
		<form name="search" action="/cgi-bin/calcular.py" method="get">
			<div class="select-wrapper select-big">
				<p>
					 Ubicación
				</p>



				<select class='elselect'>

					<option value = "">---Selecciona---</option>

				    <?php
				    $consulta_ubicacion = mysqli_query($con,"select neighborhood from rentcoach ORDER BY id DESC");
				    $num_ubicacion=mysqli_num_rows($consulta_ubicacion);

				    for($i=0; $i<$num_ubicacion; $i++) {
				    	$res_ubicacion = mysqli_fetch_array($consulta_ubicacion);
				    	?>
				    	<option value = "<?php echo $res_ubicacion['neighborhood']; ?>" ><?php echo ($res_ubicacion['neighborhood']) ?></option>
				    	
				    	<?php
				    }
				    ?>
					
				</select>

			</div>
			<input type="submit" value="Calcular" class='yellow-btn'>
		</form>
	</div>
</div>
<!-- Seccion de ultimos listados -->
<div class="recent-listings">
	<div class="container">
		<div class="title-box">
			<h3>Propiedades Destacadas</h3>
			<div class="bordered">
			</div>
		</div>
		<div class="row listings-items-wrapper">
			<div class="col-md-4 listing-single-item">
				<div class="item-inner">
					<div class="image-wrapper">
						<img src="img/piso1.jpg" alt="gallery">
						<a href="#" class='fa fa-home property-type-icon'></a>
						<a href="#" class='featured'><i class='fa fa-star'></i>Destacados</a>
					</div>
					<div class="desc-box">
						<h4><a href="#">Carrer de Aragó 123</a></h4>
						<ul class="slide-item-features item-features">
							<li><span class="fa fa-arrows-alt"></span>90m2</li>
							<li><span class="fa fa-male"></span>2 baños</li>
							<li><span class="fa fa-inbox"></span>3 habitaciones</li>
						</ul>
						<div class="buttons-wrapper">
							<a href="#" class="yellow-btn">700€</a>
							<a href="#" class="gray-btn"><span class="fa fa-file-text-o"></span>Detalles</a>
						</div>
						<div class="clearfix">
						</div>
					</div>
				</div>
			</div>
			<!-- /Single-item -->
			<div class="col-md-4 listing-single-item">
				<div class="item-inner">
					<div class="image-wrapper">
						<img src="img/piso1.jpg" alt="gallery">
						<a href="#" class='fa fa-building-o property-type-icon'></a>
					</div>
					<div class="desc-box">
						<h4><a href="#">Gran Via de Les Corts Catalanes 585</a></h4>
						<ul class="slide-item-features item-features">
							<li><span class="fa fa-arrows-alt"></span>80 m2</li>
							<li><span class="fa fa-male"></span>2 baños</li>
							<li><span class="fa fa-inbox"></span>3 habitaciones</li>
						</ul>
						<div class="buttons-wrapper">
							<a href="#" class="yellow-btn">900€</a>
							<a href="#" class="gray-btn"><span class="fa fa-file-text-o"></span>Detalles</a>
						</div>
						<div class="clearfix">
						</div>
					</div>
				</div>
			</div>
			<!-- /Single-item -->
			<div class="col-md-4 listing-single-item">
				<div class="item-inner">
					<div class="image-wrapper">
						<img src="img/piso1.jpg" alt="gallery">
						<a href="#" class='fa fa-home property-type-icon'></a>
					</div>
					<div class="desc-box">
						<h4><a href="#">Paseo de Gracia 123</a></h4>
						<ul class="slide-item-features item-features">
							<li><span class="fa fa-arrows-alt"></span>50 m2</li>
							<li><span class="fa fa-male"></span>2 baños</li>
							<li><span class="fa fa-inbox"></span>3 habitaciones</li>
						</ul>
						<div class="buttons-wrapper">
							<a href="#" class="yellow-btn">700€</a>
							<a href="#" class="gray-btn"><span class="fa fa-file-text-o"></span>Detalles</a>
						</div>
						<div class="clearfix">
						</div>
					</div>
				</div>
			</div>
			
		</div>
	</div>
</div>


<div class="bottom-strip">
	<div class="container">
		<div class="col-md-4">
			<p class='pull-left'>
				 © 2016 Rentcoach.us Derechos Reservados.
			</p>
		</div>
		<div class="col-md-4 bottom-strip-middle">
			<a href="#top" class='fa fa-arrow-circle-up' id='backtop-btn'></a>
		</div>
		<div class="col-md-4">
			<p class='pull-right'>
				 Agile Data Science Project
			</p>
		</div>
	</div>
</div>
<!-- Javascript -->
<script type="text/javascript" src="js/jquery-2.1.0.min.js"></script>
<script type="text/javascript" src="js/bootstrap.min.js"></script>
<script type="text/javascript" src="js/jquery.flexslider-min.js"></script>
<script type="text/javascript" src="js/select.min.js"></script>
<script type="text/javascript" src="js/owl.carousel.min.js"></script>
<script type="text/javascript" src="js/script.js"></script>
</body>
</html>