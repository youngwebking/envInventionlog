window.requestAnimFrame = (function(callback) {
        return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
        function(callback) {
          window.setTimeout(callback, 1000 / 60);
        };
      })();

      /*
       * Gear constructor
       */
      function Gear(config) {
        this.x = config.x;
        this.y = config.y;
        this.outerRadius = config.outerRadius;
        this.innerRadius = config.innerRadius;
        this.midRadius = config.midRadius;
        this.holeRadius = config.holeRadius;
        this.numTeeth = config.numTeeth;
        this.theta = config.theta;
        this.thetaSpeed = config.thetaSpeed / 1000;
        this.lightColor = config.lightColor;
        this.darkColor = config.darkColor;
        this.clockwise = config.clockwise;
      }
      /*
       * Gear draw method
       */
      Gear.prototype.draw = function() {
        var canvas = document.getElementById('rotating-gears');
        var context = canvas.getContext('2d');

        context.save();
        var numPoints = this.numTeeth * 2;
        // draw gear teeth
        context.beginPath();
        context.lineJoin = 'bevel';
        for(var n = 0; n < numPoints; n++) {

          var radius = null;

          if(n % 2 == 0) {
            radius = this.outerRadius;
          }
          else {
            radius = this.innerRadius;
          }

          var theta = this.theta;
          theta += ((Math.PI * 2) / numPoints) * (n + 1);

          var x = (radius * Math.sin(theta)) + this.x;
          var y = (radius * Math.cos(theta)) + this.y;

          if(n == 0) {
            context.moveTo(x, y);
          }
          else {
            context.lineTo(x, y);
          }
        }

        context.closePath();
        context.lineWidth = 5;
        context.strokeStyle = this.darkColor;
        context.stroke();

        // draw gear body
        context.beginPath();
        context.arc(this.x, this.y, this.midRadius, 0, 2 * Math.PI, false);

        var grd = context.createLinearGradient(this.x - 100, this.y - 100, this.x + 100, this.y + 100);
        grd.addColorStop(0, this.lightColor);
        grd.addColorStop(1, this.darkColor);
        context.fillStyle = grd;
        context.fill();
        context.lineWidth = 5;
        context.strokeStyle = this.darkColor;
        context.stroke();

        // draw gear hole
        context.beginPath();
        context.arc(this.x, this.y, this.holeRadius, 0, 2 * Math.PI, false);
        context.fillStyle = 'white';
        context.fill();
        context.strokeStyle = this.darkColor;
        context.stroke();
        context.restore();
      };
      function animate(gears, lastTime) {
        var canvas = document.getElementById('rotating-gears');
        var context = canvas.getContext('2d');

        // update
        var time = (new Date()).getTime();
        var timeDiff = time - lastTime;

        for(var i = 0; i < gears.length; i++) {
          var gear = gears[i];

          if(gears[i].clockwise) {
            gears[i].theta -= (gear.thetaSpeed * timeDiff);
          }
          else {
            gears[i].theta += (gear.thetaSpeed * timeDiff);
          }
        }

        // clear
        context.clearRect(0, 0, canvas.width, canvas.height);

        // draw
        for(var i = 0; i < gears.length; i++) {
          gears[i].draw();
        }

        // request new frame
        requestAnimFrame(function() {
          animate(gears, time);
        });
      }
