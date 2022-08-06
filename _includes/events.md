
    <section id="events" class="portfolio section-bg">
      <div class="container">

        <div class="section-title">
          <h2>Events</h2>
          <p>Please consider supporting the North Carolina Baroque Orchestra by making a tax-deductible donation today. Your generous gifts allow us to bring our period-instrument performances of the gorgeous music of the 17th and 18th centuries to audiences across the southeastern United States!</p>
        </div>

        <div class="row" data-aos="fade-up">
          <div class="col-lg-12 d-flex justify-content-center">
            <ul id="portfolio-flters">
              <li data-filter="*">All</li>
              <li data-filter=".filter-upcoming" class="filter-active">Upcoming</li>
              <li data-filter=".filter-past">Past</li>
            </ul>
          </div>
        </div>

        <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="100">

        {% assign numEvents = 0 %}
        {% for event in site.data.events %}

          <div class="col-lg-4 col-md-6 portfolio-item filter-upcoming">
            <div class="portfolio-wrap">
              <h4>{{ event.heading }}</h4>
              <h5>{{ event.eventdate }}</h5>
              <h5>{{ event.eventtime }}</h5>
              <p>{{ event.location }}</p>
              <p>{{ event.description }}</p>
              <div class="portfolio-links">
                <a href="assets/img/portfolio/portfolio-1.jpg" data-gallery="portfolioGallery" class="portfolio-lightbox" title="App 1"><i class="bx bx-plus"></i></a>
                {% if event.eventurl %}
                    <a href="{{ event.eventurl }}" target="_blank" title="More Details"><i class="bx bx-link"></i></a>
                {% endif %}
              </div>
            </div>
          </div>
        {% endfor %}

        </div>

      </div>
    </section>