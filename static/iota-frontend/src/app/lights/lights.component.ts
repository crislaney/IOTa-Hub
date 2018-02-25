import { Component, OnInit } from '@angular/core';
import { Light } from '../light';
@Component({
  selector: 'app-lights',
  templateUrl: './lights.component.html',
  styleUrls: ['./lights.component.css']
})
export class LightsComponent implements OnInit {


  colorChange(val: number) {
    console.log("Slider changed!");
    console.log(val)
  };

  briChange(val: number) {
    console.log("Slider changed!");
    console.log(val)
  };

  satChange(val: number) {
    console.log("Slider changed!");
    console.log(val)
  };
  light1: Light = {
    id: 5,
    name: "Cris Bedroom 1",
    xy:[0.004, 0.05]
  };

  constructor() { }

  ngOnInit() {
  }

}
