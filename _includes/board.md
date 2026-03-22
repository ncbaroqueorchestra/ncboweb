
    <section id="board" class="services">
      <div class="container">

        <div class="section-title">
          <h2>Board Members</h2>
        </div>

        <div class="row">
          {% assign board_sorted = site.data.board | sort: "order" %}
          {% for member in board_sorted %}
          <div class="col-lg-4 col-md-6 icon-box" data-aos="fade-up">
            <div class="icon"><i class="bi bi-person-circle"></i></div>
            <h4 class="title">{{ member.boardmember }}</h4>
            {% if member.position != '' %}
            <p class="description">{{ member.position }}</p>
            {% endif %}
          </div>
          {% endfor %}
        </div>
      </div>
    </section><!-- End Board Section -->

