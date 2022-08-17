
    <section id="events" class="portfolio section-bg">
      <div class="container">

        <div class="section-title">
          <h2>Upcoming Events</h2>
          <p>Click on an event for more details!</p>
        </div>

        <div class="col-lg-6 offset-md-1 accordion" id="eventAccordion">
            {% assign numEvents = 0 %}
            {% for event in site.data.events %}
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading{{numEvents}}">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#details{{numEvents}}" aria-expanded="false" aria-controls="details{{numEvents}}">
                    <div>
                        <h4>{{ event.heading }}</h4>
                        <h5>{{ event.eventdate }}{% if event.eventtime%} &mdash; {% endif %}{{ event.eventtime }}</h5>
                    </div>
                  </button>
                </h2>
                <div id="details{{numEvents}}" class="accordion-collapse collapse" aria-labelledby="heading{{numEvents}}" data-bs-parent="#eventAccordion">
                  <div class="accordion-body" style="background-color:#f6f8fd">
                    <div class="row">
                        <p>{{ event.description }}</p>
                    </div>
                    <div class="row">
                      <p>{{ event.venue }}<br/>
                      {{ event.address }}
                      </p>
                      <div class="content">
                          {% if event.mapurl %}
                              <a class="btn btn-outline-primary" role="button" href="{{ event.mapurl }}" target="_blank">Map</a>
                          {% endif %}
                          {% if event.eventdetailsurl %}
                              <a class="btn btn-outline-primary" role="button" href="{{ event.eventdetailsurl }}" target="_blank">More Details</a>
                          {% endif %}
                          {% if event.ticketurl %}
                              <a class="btn btn-primary" role="button" aria-expanded="false" href="{{ event.ticketurl }}" target="_blank">Buy Tickets</a>
                          {% endif %}
                      </div>
                    </div>
                  </div>
                </div>
            </div>
            {% assign numEvents = numEvents | plus: 1 %}
            {% endfor %}

        </div>

      </div>
    </section>
