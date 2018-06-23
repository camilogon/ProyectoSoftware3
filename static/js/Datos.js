function materias(idcurso, nombrecurso){

   $.get("/Actividad/ListarMateria",{"id":idcurso},function (response) {
       var materia  = JSON.parse(response);
       //console.log(materia);
       $("#lista-materias").html("");
       var tipo =nombrecurso;
       console.log(document.getElementById(nombrecurso.id));
       console.log(nombrecurso.id);
       console.log(idcurso)
        var x = "#"+ idcurso;

       if (confirm(nombrecurso.id)){

           // $("#lista-materias").append(nombrecurso);
       for(var i=0;i<materia.length;i++){

           var template = "<li class=\"fa fa-bar-chart-o\" onclick='metodito("+materia[i]['pk']+")'> "+materia[i]['fields']['Nombre']+"</li>";
             if(! $(x).empty()){
            $(x).removeChild(template);
        }

           $(x).append(template);


       }

       }
    });
}
/*
$(function () {
    /*$.post("/Actividad/ListarMateria",{"hola":"navas"},function (response) {
        console.log(response);
    });


});
*/
