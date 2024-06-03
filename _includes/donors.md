<section class="portfolio section-bg" id="events">
    <div class="container">

        <div class="section-title">
            <h2>Donors</h2>
        </div>
    </div>

    <div class="container">
        
        <div class="container">
        <div class="row row-cols-1  row-cols-md-3 g-4">
        {% assign currentLevel = 0 %}
        {% for donor in site.data.donors %}
            {% if currentLevel != donor.levelnumber %}
                {% if currentLevel != 0 %}
                        </div>
                    </div>
                </div>
                {% endif %}
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-text">{{ donor.level }}</h5>
                {% assign currentLevel = donor.levelnumber %}
            {% endif %}
        
                        <p class="card-title" style="margin-left:10px">{{ donor.donorname }}</p>
                        

        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>

</section>
