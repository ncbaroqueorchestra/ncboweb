<section class="portfolio section-bg" id="events">
    <div class="container">

        <div class="section-title">
            <h2>Upcoming Events</h2>
        </div>
    </div>

    <div class="container">
        
        <div class="row row-cols-1 row-cols-md-3 g-4">
        {% assign numEvents = 0 %}
        {% for event in site.data.events %}
            <div class="col">
                <div class="card" >
                    <!-- <img src="..." class="card-img-top" alt="..."> -->
                    <div class="card-body">
                        {% if event.eventimage %}
                            <img src="{{ event.eventimage }}" class="card-img-top" alt="...">
                        {% endif %}
                        <h5 class="card-title">{{ event.heading }}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">{{ event.eventdate }} - {{ event.eventtime }}</h6>
                        <p class="card-text">{{ event.description }}</p>
                        <p class="card-text">{{ event.venue }}</p>

                        {% if event.mapurl %}
                            <a href="{{ event.mapurl }}" target="_blank">
                                <p class="card-text">{{ event.address }}</p>
                            </a>
                        {% else %}
                            <p class="card-text">{{ event.address }}</p>
                        {% endif %}
                        <!-- Optional links for tickets and details -->
                        <div style="padding-top:20px">
                            {% if event.ticketurl %}
                                <a class="btn btn-primary" href="{{ event.ticketurl }}" target="_blank">Buy Tickets</a>
                            {% endif %}
                            {% if event.eventdetailsurl %}
                                <a class="btn btn-light" href="{{ event.eventdetailsurl }}" target="_blank">More Details</a>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
            {% assign numEvents = numEvents | plus: 1 %}
        {% endfor %}
        </div>
    </div>

</section>
