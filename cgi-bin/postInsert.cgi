#!/usr/bin/perl -WT

# inserimento dei commenti della home nel file xml commenti
# carico le librerie
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
#use CGI::Session;
use XML::LibXML;
use File::Copy;
use URI;

use Time::Local 'timelocal_nocheck';


sub leggi_post()
{   
    my($buffer, $nome, $valore, @pairs, %DATI);
    
    read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    #
    # Suddivide la richiesta in un array di coppie «nome=valore».
    #
    @pairs = split (/&/, $buffer);
    #
    # Elabora ogni coppia contenuta nell'array.
    #
    foreach my $elemento (@pairs)
      {
        #
        # Scompone la coppia.
        #
        ($nome, $valore) = split ('=', $elemento);
        #
        # Trasforma «+» in spazio.
        #
        $valore =~ tr/+/ /;
        $nome =~ tr/+/ /;
        #
        # Trasforma «%hh» nel carattere corrispondente.
        #
        $nome   =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        $valore =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        #
        # Aggiunge la coppia decodificata in un hash.
        #
        $DATI{$nome} = $valore;
      }
      # Restituisce l'hash delle coppie ( nome => valore )
      return (%DATI);
}

# leggo i dati dal POST e li inserisco nell'hash DATI
my %DATI = &leggi_post();

if(!%DATI){
    print redirect("home.xhtml");
}

# creo e inizializzo le variabili con i dati del POST
my $user = "io";   #$DATI{'...'}; username dalla sessione ...
my $contenuto;
my $post="post";
foreach my $key (keys %DATI) { 
    if($key =~ /nuovoCommento([0-9]*)/){
        $contenuto = $DATI{$key};
        my $numId = substr $key, 13;
        $post= $post.$numId; 
    }
}

(my $sec,my $min,my $ore,my $giom,my $mese,my $anno,my $gios,my $gioa,my $oraleg)=localtime();
my @abbr = qw( Gen Feb Mar Apr Mag Giu Lug Ago Set Ott Nov Dic );
$anno+=1900;
my $data = " $giom $abbr[$mese] $anno alle ore $ore.$min"; #"19-01-2015";   #$DATI{'...'}; data di inserimento

#===============================================================================
# Cerco nel file utenti.xml se l'utente è gia registrato
my $file = "../XML/commenti.xml";
open(IN, $file) or die $!;
flock(IN, 2); # file lock per prevenire accessi concorrenti a commenti.xml

# creazione oggetto parser
my $parser = XML::LibXML->new();
#
# apertura file e lettura input
my $doc = $parser->parse_file($file);

# estrazione radice
my $root = $doc->getDocumentElement;

    # Inserisco il nuovo utente nel file utenti.xml
    my $commentoXML = XML::LibXML::Element->new('commento'); 
    my $userXML = XML::LibXML::Element->new('user');
    my $postXML = XML::LibXML::Element->new('post');
    my $dataXML = XML::LibXML::Element->new('data');
    my $contenutoXML = XML::LibXML::Element->new('contenuto');

    $userXML->appendText( $user );
    $postXML->appendText( $post );
    $dataXML->appendText( $data );
    $contenutoXML->appendText( $contenuto );

    $commentoXML->appendChild($userXML);
    $commentoXML->appendChild($postXML);
    $commentoXML->appendChild($dataXML);
    $commentoXML->appendChild($contenutoXML);

    #my $commentiXML = $root -> getElementsbyTagName('commenti');
    #$commentiXML->appendChild($commentoXML);

    $root->appendChild($commentoXML);
    
# scrittura su file
open(OUT,">$file") or die $!;
print OUT $doc->toString;
close(OUT);        
close(IN); # libera il lock 
# inserimento con successo
#} 
my $query=new CGI;
print $query->redirect("../htdocs/home.xhtml");
