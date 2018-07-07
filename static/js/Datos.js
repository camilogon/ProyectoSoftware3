function materias(idcurso, nombrecurso){
   $.get("/Actividad/ListarMateria",{"id":idcurso},function (response) {
       var materia  = JSON.parse(response);
       $("#lista-materias").html("");
       var tipo =nombrecurso;
       var x = "#"+ idcurso;
       if (confirm(nombrecurso.id)){
       for(var i=0;i<materia.length;i++){
           //var url1 = '{% url ListarActividad  "'+materia[i]['pk']+'" %}';
           var template = "<li><a href='http://localhost:8000/Actividad/ListarActividad/"+materia[i]['pk']+"'> "+materia[i]['fields']['Nombre']+"</li>";
           if(! $(x).empty()){
              $(x).removeChild(template);
           }
           $(x).append(template);
       }

       }
    });
}
function materiasCuestionario(idcurso, nombrecurso){
   $.get("/Cuestionario/ListarMateria",{"id":idcurso},function (response) {
       var materia  = JSON.parse(response);
       $("#lista-materias").html("");
       var tipo =nombrecurso;
       var x = "#"+ idcurso;
       if (confirm(nombrecurso.id)){
       for(var i=0;i<materia.length;i++){
           //var url1 = '{% url ListarActividad  "'+materia[i]['pk']+'" %}';
           var template = "<li><a href='http://localhost:8000/Cuestionario/ListarCuestionario/"+materia[i]['pk']+"'> "+materia[i]['fields']['Nombre']+"</li>";
           if(! $(x).empty()){
              $(x).removeChild(template);
           }
           $(x).append(template);
       }

       }
    });
}
/*
function EnviarMaterias(){
    var idTema=  $('#CodigoTema').val()
    console.log("soy El tema "+ idTema)
   $.post("/Cuestionario/Crear",{"CodigoTema":idTema},function (response) {
    });
}*/
/*
$(function () {
    /*$.post("/Actividad/ListarMateria",{"hola":"navas"},function (response) {
        console.log(response);
    });


});
*/

