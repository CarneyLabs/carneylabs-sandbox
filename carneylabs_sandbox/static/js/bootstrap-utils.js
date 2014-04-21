var ButtonColor = {
    DEFAULT: "btn-default",
    PRIMARY: "btn-primary",
    INFO: "btn-info",
    SUCCESS: "btn-success",
    WARNING: "btn-warning",
    DANGER: "btn-danger",
    INVERSE: "btn-inverse"
};

var ButtonSize = {
    LARGE: "btn-large",
    MEDIUM: "btn-medium",
    SMALL: "btn-small",
    MINI: "btn-mini"
};

function create_button(button_label,
                       button_color,
                       button_size)
{
    var button = $("<button class='btn' type='button'></button>").html(button_label);
    button.addClass(button_color || ButtonColor.DEFAULT);
    button.addClass(button_size || ButtonSize.MEDIUM);

    //console.log("Button created: " + button);

    return button;
}

var AlertTheme = {
    SUCCESS: "alert-success",
    INFO: "alert-info",
    WARNING: "alert-warning",
    DANGER: "alert-danger"
};

function create_alert(message,
                      alert_theme)
{
    var alert = $(
        "<div class='alert alert-dismissable fade in'>" +
            "<button type='button' class='close' data-dismiss='alert'>&times;</button>" +
            message +
        "</div>"
    );

    alert.addClass(alert_theme || AlertTheme.WARNING);

    //console.log("Alert created: " + alert);

    return alert;
}

function create_carousel(slides, interval) {
    var carousel = $(
        "<div class='carousel slide' data-ride='carousel'>" +
            "<div class='carousel-inner'></div>" +
        "</div>"
    );

    var inner = carousel.find("div.carousel-inner");

    for(var i = 0, num_slides = slides.length; i < num_slides; i++) {
        var slide = slides[i];
        slide.appendTo(inner);
    }

    carousel.carousel({
        interval: interval || false
    });

    //console.log("Carousel created: " + carousel);

    return carousel;
}

function create_carousel_slide(active) {
    var slide = $("<div class='item'></div>");

    if(active) {
        slide.addClass("active");
    }

    //console.log("Carousel slide created: " + slide);

    return slide;
}

function create_progress_bar(progress) {
    var progress_bar = $(
        "<div class='progress'>" +
            "<div class='progress-bar' role='progressbar'></div>" +
            "<p></p>" +
        "</div>"
    );

    if(progress > 0 && progress < 1) {
        progress *= 100;
    }

    progress = Math.floor(progress);

    var progress_string = progress.toString() + "%";

    progress_bar.find("div.progress-bar").css("width", progress_string);

    //console.log("Progress bar created: " + progress_bar);

    return progress_bar;
}

function create_pop_up(id,
                       header,
                       body,
                       footer)
{
    var pop_up = $(
        "<div class='modal fade'>" +
            "<div class='modal-dialog'>" +
                "<div class='modal-content'></div>" +
            "</div>" +
        "</div>"
    );

    pop_up.attr("id", id);

    var pop_up_content = pop_up.find(".modal-content");

    if(header) {
        header.appendTo(pop_up_content);
    }

    if(body) {
        body.appendTo(pop_up_content);
    }

    if(footer) {
        footer.appendTo(pop_up_content);
    }

    //console.log("Pop up created: " + pop_up);

    return pop_up;
}

function create_pop_up_header(title) {
    var pop_up_header = $(
        "<header class='modal-header'>" +
            "<button type='button' class='close' data-dismiss='modal'>&times;</button>" +
            "<h4 class='modal-title'>" + title + "</h4>" +
        "</header>"
    );

    //console.log("Pop up header created: " + pop_up_header);

    return pop_up_header;
}

function create_pop_up_body(content) {
    var pop_up_body = $(
        "<div class='modal-body'></div>"
    );

    pop_up_body.append(content);

    //console.log("Pop up body created: " + pop_up_body);

    return pop_up_body;
}

function create_pop_up_footer(negative_button_label,
                              positive_button_label)
{
    var pop_up_footer = $(
        "<footer class='modal-footer'></footer>"
    );

    if(negative_button_label) {
        $("<button type='button' class='btn btn-default' data-dismiss='modal'></button>")
            .text(negative_button_label)
            .appendTo(pop_up_footer);
    }

    if(positive_button_label) {
        $("<button type='button' class='btn btn-primary'></button>")
            .text(positive_button_label)
            .appendTo(pop_up_footer);
    }

    //console.log("Pop up footer created: " + pop_up_footer);

    return pop_up_footer;
}