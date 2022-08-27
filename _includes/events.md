<section class="portfolio section-bg" id="events">
    <div class="container">

        <div class="section-title">
            <h2>Upcoming Events</h2>
            <p>Click on an event for more details!</p>
        </div>
    </div>

    <div class="col-lg-8 offset-md-1 accordion" data-aos="fade-up" id="eventAccordion">
        {% assign numEvents = 0 %}
        {% for event in site.data.events %}
            <h3 class="accordion-header" id="heading{{numEvents}}">
                {% assign oddEven = numEvents | modulo:2 %}
                {% if oddEven == 0 %}
                    <button aria-controls="details{{numEvents}}" aria-expanded="false" class="accordion-button collapsed" data-bs-target="#details{{numEvents}}" data-bs-toggle="collapse" type="button" style="background-color: #d9d8f4;">
                {% else %}
                    <button aria-controls="details{{numEvents}}" aria-expanded="false" class="accordion-button collapsed" data-bs-target="#details{{numEvents}}" data-bs-toggle="collapse" type="button">
                {% endif %}
                    <div>
                        <h5>{{ event.heading }}</h6>
                        <h6>{{ event.eventdate }}
                            {% if event.eventtime%}
                                &mdash;
                            {% endif %}
                            {{ event.eventtime }}</h6>
                    </div>
                </button>
            </h3>

            <div aria-labelledby="heading{{numEvents}}" data-bs-parent="heading{{numEvents}}" class="accordion-collapse collapse" id="details{{numEvents}}">
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
            {% assign numEvents = numEvents | plus: 1 %}
            {% if numEvents > 4 %}
                {% break %}
            {% endif %}
        {% endfor %}
        </div>
    </div>
    {% if numEvents > 4 %}
        <div class="col-md-10 text-center" data-aos="fade-up" style="padding-top:20px">
            <a class="btn btn-primary" role="button" aria-expanded="false" href="events">See All Events</a>
        </div>
    {% endif %}
</section>

