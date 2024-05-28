<section class="portfolio section-bg" id="events">
    <div class="container">

        <div class="section-title">
            <h2>Donors</h2>
        </div>
    </div>

    <div class="container">
        
        <div class="container" style="padding-top:40px">
        <h1>Donors</h1>
        <div class="row row-cols-1 row-cols-md-3 g-4">
        {% for donor in site.data.donors %}
            <div class="col">
                <div class="card" >
                    <!-- <img src="..." class="card-img-top" alt="..."> -->
                    <div class="card-body">
                        <h5 class="card-title">{{ donor.donorname }}</h5>
                        <p class="card-text">{{ donor.level }}</p>
                        
                    </div>
                </div>
            </div>
        {% endfor %}
        </div>
    </div>

</section>
