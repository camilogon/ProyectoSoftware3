function materias(idcurso, nombrecurso){
   $.get("/Actividad/ListarMateria",{"id":idcurso},function (response) {
       var materia  = JSON.parse(response);
       $("#lista-materias").html("");
       var tipo =nombrecurso;
       var x = "#"+ idcurso;
       if (confirm(nombrecurso.id)){
           // $("#lista-materias").append(nombrecurso);
       for(var i=0;i<materia.length;i++){
           //var url1 = '{% url ListarActividad  "'+materia[i]['pk']+'" %}';
           var template = "<li class=\"fa fa-bar-chart-o\"><a href='http://localhost:8000/Actividad/ListarActividad/"+materia[i]['pk']+"'> "+materia[i]['fields']['Nombre']+"</li>";
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
