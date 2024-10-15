<section class="portfolio section-bg" id="past_events">
    <div class="container">
        <div class="section-title">
            <div class="d-flex align-items-top" style="cursor:pointer" id="toggle-past-events">
                <h2 class="mr-2">Past Events</h2>
                <p class="card-text mb-0 text-muted" style="padding-top: 12px; padding-left: 5px;">Click to show/hide</p>
            </div>
        </div>
    </div>

    <div class="container mt-2" style="display: none;" id="events-container" >
            {% for event in site.data.past_events %}
            <div class="row" style="padding: 5px 0;">
                <div class="col-md-4">
                    <p class="card-text">{{ event.eventdate}}</p>
                </div>
                <div class="col-md-4">
                    <p class="card-text">{{ event.heading}}</p>
                </div>
                <div class="col-md-4">
                    <p class="card-text">{{ event.venue}}</p>
                </div>
            </div>
            <div class="row border-bottom" style="margin-top: 3px;">
                <div class="col-12">
                    <p class="card-subtitle text-muted">{{ event.description}}</p>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script>
    $(document).ready(function() {
        $('#toggle-past-events').click(function() {
            $('#events-container').toggle(); // Toggles the visibility of the events container
        });
    });
</script>

