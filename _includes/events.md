
    <section id="events" class="portfolio section-bg">
      <div class="container">

        <div class="section-title">
          <h2>Upcoming Events</h2>
          <p>Please consider supporting the North Carolina Baroque Orchestra by making a tax-deductible donation today. Your generous gifts allow us to bring our period-instrument performances of the gorgeous music of the 17th and 18th centuries to audiences across the southeastern United States!</p>
          <br/>
          <p>Click on an event for more details!</p>
        </div>

        <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="100">

        {% assign numEvents = 0 %}
        {% for event in site.data.events %}

            <div class="col-lg-4 col-md-6 portfolio-item">
              <div class="portfolio-wrap">
                <a class="portfolio-content" data-toggle="modal" data-target="#eventdetails{{numEvents}}" href="">
                    <h4>{{ event.heading }}</h4>
                    <h5>{{ event.eventdate }}{% if event.eventtime%}&mdash;{% endif %}{{ event.eventtime }}</h5>
                </a>
                {% include eventpopupwidget.html %}
              </div>
          </div>
          {% assign numEvents = numEvents | plus: 1 %}
        {% endfor %}

        </div>

      </div>
    </section>